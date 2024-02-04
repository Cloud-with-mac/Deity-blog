from About_US.models import SocialLink
from .models import Category


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


# Make sure you go to the project settings and add the get_categories and get_social_links on the template

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)
