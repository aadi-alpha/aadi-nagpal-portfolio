from django.contrib import admin
from django.contrib import admin
from .models import (
    Profile, SocialLinks, SkillCategories, Skills,
    About, AboutPoint, Education, Principles,
    Project, ProjectFeature, Achievement, Certificate, ContactMessage
)



# -------------------------
# Profile
# -------------------------
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "profession", "college")
    search_fields = ("name", "title", "college")


# -------------------------
# Social Links
# -------------------------
@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "icon")
    search_fields = ("name",)


# -------------------------
# Skills
# -------------------------
@admin.register(SkillCategories)
class SkillCategoriesAdmin(admin.ModelAdmin):
    list_display = ("category_name", "slug")
    search_fields = ("category_name", "description")
    prepopulated_fields = {"slug": ("category_name",)}


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


# -------------------------
# About
# -------------------------
class AboutPointInline(admin.TabularInline):
    model = AboutPoint
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id",)
    inlines = [AboutPointInline]


@admin.register(AboutPoint)
class AboutPointAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


# -------------------------
# Education
# -------------------------
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "title", "institution", "period",
        "status", "is_completed"
    )
    list_filter = ("status", "is_completed")
    search_fields = ("title", "institution")


# -------------------------
# Principles
# -------------------------
@admin.register(Principles)
class PrinciplesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


# -------------------------
# Projects
# -------------------------
class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title", "category", "status",
        "status_type", "featured"
    )
    list_filter = ("status_type", "category", "featured")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectFeatureInline]


@admin.register(ProjectFeature)
class ProjectFeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "number")
    list_filter = ("project",)
    search_fields = ("title", "description")


# -------------------------
# Achievements
# -------------------------
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "title", "badge", "category",
        "date", "position", "is_featured"
    )
    list_filter = ("badge", "category", "is_featured")
    search_fields = ("title", "category", "description")
    list_editable = ("is_featured",)
    ordering = ("position",)


# -------------------------
# Certificates
# -------------------------
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "title", "provider", "year",
        "type", "is_featured"
    )
    list_filter = ("year", "type", "provider", "is_featured")
    search_fields = ("title", "provider", "description")
    list_editable = ("is_featured",)
    ordering = ("-year",)
# Register your models here.

# -------------------------
# Contact Message
# -------------------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject")
    search_fields = ("full_name", "email", "subject")