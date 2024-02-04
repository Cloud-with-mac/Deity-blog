from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

from About_US.models import About
from blog_app.models import Category, Blog
from django.db.models import Q

def home(request):
    featured_post = Blog.objects.filter(is_featured=True)  # .order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status=1)

    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_post': featured_post,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)


def post_by_category(request, category_id):
    post = Blog.objects.filter(status=1, category=category_id)

    category = get_object_or_404(Category, id=category_id)

    # try:
    #     category = get_object_or_404(Category, id=category_id)
    # except:
    #     return redirect('home')
    # use et_object_or_404 when you want to show 404 error page if the category does not exist
    # category = get_object_or_404(Category, id=category_id)
    context = {
        'post': post,
        'category': category
    }
    return render(request, 'postbycategory.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status=1)
    context = {
        'single_blog': single_blog
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    blog_title = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status=1)
    context = {
        'blog': blog_title,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)
