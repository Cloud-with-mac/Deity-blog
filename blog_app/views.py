from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

from blog_app.models import Category, Blog


def home(request):
    featured_post = Blog.objects.filter(is_featured=True)  # .order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status=1)
    context = {
        'featured_post': featured_post,
        'posts': posts
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
