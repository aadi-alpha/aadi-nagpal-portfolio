from django.shortcuts import render
from . import data
# Create your views here.
from .models import Profile, SocialLinks , About, AboutPoint, Education, Principles, Achievement, Certificate,Skills, SkillCategories
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm

def home(req):
    profile = Profile.objects.get()
    
    social_links = SocialLinks.objects.filter(profile = profile.id)
    
    context = {
        "profile": profile,
        "social_links":social_links,
        "skills": Skills.objects.filter(is_featured=True),
        "achievements":Achievement.objects.filter(is_featured = True),
        "certificates": Certificate.objects.filter(is_featured = True)
        
    }
    return render(req,'portfolio/home.html',context)

def about(req):
    about = About.objects.get()
    aboutPoint = AboutPoint.objects.filter(about=about.id)
    education = Education.objects.order_by("-id")
    principles = Principles.objects.all()
    context ={
        "about": about,
        "aboutPoint":aboutPoint,
        "education":education,
        "principles":principles
    }
    return render(req, 'portfolio/about.html', context)

def skills(req):
    skills = SkillCategories.objects.prefetch_related("skills_set")
    
   
    context = {
        "skills":skills,
        
    }
    return render(req, 'portfolio/skills.html', context)

def project(req):
    context = {
        "projects":data.PROJECTS
    }
    return render(req, 'portfolio/projects.html',context)


def achievement(req):
    context = {
        "achievements": Achievement.objects.all(),
        "first_count":Achievement.objects.filter(position=1).count()

    }
    return render(req, 'portfolio/achievements.html',context)

def certificate(req):
    context = {
        "certificates" : Certificate.objects.all()
    }
    return render(req, 'portfolio/certificates.html',context)

def contact(request):

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your message has been sent successfully!"
            )
            return redirect("contact")
        else:
            messages.error(
                request,
                "Please correct the errors and try again."
            )
    else:

        form = ContactMessageForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "portfolio/contact.html",
        context
    )


def page_not_found(request,*args, **kwargs):
    return render(
        request,
        "portfolio/404.html",
        
    )