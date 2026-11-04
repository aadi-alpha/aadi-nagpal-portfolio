
from .models import Profile, SocialLinks

def global_portfolio_data(request):
    profile = Profile.objects.get()
        
    social_links = SocialLinks.objects.filter(profile = profile.id)
    return {
        "profile": profile,
        "social_links": social_links
    }