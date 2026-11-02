from django.urls import path  
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home' ), 
    path('about', views.about, name='about' ),
    path('contact', views.contact, name='contact' ),
    path('skills', views.skills, name='skills' ),
    path('certificates', views.certificate, name='certificates' ),
    path('achievements', views.achievement, name='achievements' ),
    path('project', views.project, name='projects' ),
    path('<path:unknown>', views.page_not_found),
    
    
]
