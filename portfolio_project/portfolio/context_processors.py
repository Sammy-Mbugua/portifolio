from .models import Profile, SocialLink

def portfolio_context(request):
    """Global context processor for portfolio data"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    social_links = SocialLink.objects.all()
    
    return {
        'site_profile': profile,
        'site_social_links': social_links,
    }