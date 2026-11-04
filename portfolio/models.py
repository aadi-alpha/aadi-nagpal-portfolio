from django.db import models
from django.utils.text import slugify
# Create your models here.
# ============= PROFILE MODELS ==============
class Profile(models.Model):
    AVAILABILITY_CHOICES = [
        ("online", "Online"),
        ("offline", "Offline"),
    ]

 
    name = models.CharField( max_length=100)
    title = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    introduction = models.CharField(max_length=500)
    availability = models.CharField(max_length=20,  choices=AVAILABILITY_CHOICES ,default="online")

    def __str__(self):
        return self.name


class SocialLinks(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="social_links"
    )
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=300)
    url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name  



# ============= SKILLS MODELS ==============
class SkillCategories(models.Model):
    category_name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    icon = models.CharField(max_length=100)
    note = models.TextField(max_length=250)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Skills(models.Model):
    SKILL_LEVEL_CHOICES = [
        ("proficient","Proficient"),
        ("intermediate","Intermediate"),
        ("learning", "Learning"),

    ]
    category = models.ForeignKey(
        SkillCategories,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30)
    level = models.CharField(max_length=30, choices = SKILL_LEVEL_CHOICES)
    icon = models.CharField(max_length=200)
    color = models.CharField(max_length=10)
    is_featured = models.BooleanField()





# ============= ABOUT MODELS ==============
class About(models.Model):
    profile_image = models.URLField(max_length=500, blank=True)
    profile_tag = models.CharField(max_length=150)
    highlight = models.TextField()

    quote = models.TextField()
    quote_author = models.CharField(max_length=150)

    def __str__(self):
        return self.profile_tag

  


class AboutPoint(models.Model):
    about = models.ForeignKey(
        About,
        on_delete=models.CASCADE,
        related_name="points"
    )

    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.title

# ============= EDUCATION MODELS ==============

class Education(models.Model):
    EDUCATION_STATUS_CHOICES = [
        ("ongoing","Ongoing"),
        ("completed","Completed")
    ]
    period = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=EDUCATION_STATUS_CHOICES)
    is_completed = models.BooleanField(blank=True)
    title = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    institution_url = models.URLField(max_length=150, )
    description = models.TextField()
    tags = models.JSONField(default=list,blank=True)
    timeline_position = models.CharField(max_length=5)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.institution

    def save(self, *args, **kwargs ):
        self.is_completed = self.status == "completed"
        return super().save(*args, **kwargs)


# ============= PRINCIPLES MODELS ==============
class Principles(models.Model):
    title = models.CharField(max_length=150)
    icon = models.CharField(max_length=100)
    description = models.TextField()
    link_text = models.CharField(max_length=80)

    def __str__(self):
        return self.title




# ============= PROJECT MODELS ==============

class Project(models.Model):

    STATUS_TYPE_CHOICES = [
        ("featured", "Featured"),
        ("planning", "Planning"),
        ("completed", "Completed"),
        ("ongoing", "Ongoing"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    category = models.CharField(max_length=100)
    
    label = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    status_type = models.CharField(
        max_length=20,
        choices=STATUS_TYPE_CHOICES
    )

    short_description = models.TextField()
    description = models.TextField()

    technologies = models.JSONField(default=list, blank=True)

    technical_note = models.TextField(blank=True)
    note_icon = models.CharField(max_length=100, blank=True)

    image = models.CharField(max_length=255, blank=True)
    image_alt = models.CharField(max_length=200, blank=True)
    image_caption = models.CharField(max_length=200, blank=True)

    live_url = models.URLField(max_length=300, blank=True)
    github_url = models.URLField(max_length=300, blank=True)
    architecture_url = models.URLField(max_length=300, blank=True)

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    


class ProjectFeature(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="features"
    )

    number = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.project.title} - {self.title}"

    




# ============= ACHIEVEMENT MODEL ==============
class Achievement(models.Model):
    position = models.PositiveIntegerField()
    date = models.CharField(max_length=50)
    category = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    badge = models.CharField(max_length=100)
    project_tag = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    highlights = models.JSONField(default=list, blank=True)
    image = models.CharField(max_length=255, blank=True)
    image_alt = models.CharField(max_length=200, blank=True)
    certificate_url = models.URLField(max_length=300, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.badge}"


  # ============= CERTIFICATES MODEL ==============

class Certificate(models.Model):
    CERTIFICATE_TYPE_CHOICES = [
        ("certificate", "Certificate"),
        ("course", "Course Completion"),
        ("workshop", "Workshop"),
        ("internship", "Internship"),
        ("achievement", "Achievement"),
    ]
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    type = models.CharField(
        max_length=30,
        choices=CERTIFICATE_TYPE_CHOICES,
        default="certificate"
    )
    description = models.TextField()
    topics = models.JSONField(default=list, blank=True)
    image = models.CharField(max_length=255, blank=True)
    image_alt = models.CharField(max_length=200, blank=True)
    certificate_url = models.CharField(max_length=300, blank=True)
    certificate_label = models.CharField(
        max_length=100,
        default="View Certificate"
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.provider}"



class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"