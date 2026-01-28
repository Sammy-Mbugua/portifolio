from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import (
    Profile, Education, Experience, Skill, 
    Project, ContactMessage, SocialLink, SkillCategory
)
from .forms import ContactForm
#home view
def home(request):
    """Home page view"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    education = Education.objects.all()[:3]
    experiences = Experience.objects.all()[:4]
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    featured_projects = Project.objects.filter(featured=True)[:6]
    social_links = SocialLink.objects.all()
    
    context = {
        'profile': profile,
        'education': education,
        'experiences': experiences,
        'skill_categories': skill_categories,
        'projects': featured_projects,
        'social_links': social_links,
    }
    
    return render(request, 'portfolio/home.html', context)

#about view
def about(request):
    """About page view"""
    profile = Profile.objects.first()
    education = Education.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    
    context = {
        'profile': profile,
        'education': education,
        'skill_categories': skill_categories,
    }
    
    return render(request, 'portfolio/about.html', context)

#experience list view
def experience_list(request):
    """Experience list page"""
    experiences = Experience.objects.all()
    
    context = {
        'experiences': experiences,
    }
    
    return render(request, 'portfolio/experience.html', context)

#projects list view
def projects_list(request):
    """Projects list page with pagination"""
    projects = Project.objects.all()
    
    # Filter by featured if requested
    if request.GET.get('featured') == 'true':
        projects = projects.filter(featured=True)
    
    # Pagination
    paginator = Paginator(projects, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'projects': page_obj.object_list,
    }
    
    return render(request, 'portfolio/projects.html', context)

#project detail view
def project_detail(request, pk):
    """Individual project detail page"""
    project = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.exclude(pk=pk).filter(featured=True)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    
    return render(request, 'portfolio/project_detail.html', context)

#contact view
def contact(request):
    """Contact page with form"""
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('portfolio:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'profile': profile,
    }
    
    return render(request, 'portfolio/contact.html', context)


@require_POST
def contact_ajax(request):
    """AJAX endpoint for contact form"""
    form = ContactForm(request.POST)
    
    if form.is_valid():
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message!'
        })
    else:
        return JsonResponse({
            'success': False,
            'errors': form.errors
        }, status=400)


def download_resume(request):
    """Download resume file"""
    profile = Profile.objects.first()
    if profile and profile.resume:
        from django.http import FileResponse
        return FileResponse(profile.resume.open('rb'), as_attachment=True)
    else:
        messages.error(request, 'Resume not available.')
        return redirect('portfolio:home')
