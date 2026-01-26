from django.contrib import admin
from .models import (
    Profile, Education, Experience, Achievement, 
    SkillCategory, Skill, Project, ContactMessage, SocialLink
)

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1
    fields = ['description', 'order']

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['name', 'proficiency', 'order']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'location', 'updated_at']
    search_fields = ['name', 'email']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'about')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Media', {
            'fields': ('github_url', 'linkedin_url')
        }),
        ('Files', {
            'fields': ('profile_image', 'resume')
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'location']
    list_filter = ['institution']
    search_fields = ['degree', 'institution']
    date_hierarchy = 'end_date'

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'currently_working']
    list_filter = ['currently_working', 'company']
    search_fields = ['title', 'company', 'description']
    date_hierarchy = 'start_date'
    inlines = [AchievementInline]
    
    fieldsets = (
        ('Position Information', {
            'fields': ('title', 'company', 'location')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'currently_working')
        }),
        ('Details', {
            'fields': ('description',)
        }),
    )

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']
    inlines = [SkillInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category__order', 'order']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_filter = ['featured']
    search_fields = ['title', 'description', 'technologies']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'technologies')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Display Settings', {
            'fields': ('featured', 'order', 'image')
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    date_hierarchy = 'created_at'
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'order']
    list_filter = ['platform']
    ordering = ['order']
