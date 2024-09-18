from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import auth, User
from django.template.defaulttags import comment

from About_US.models import About
from blog_app.models import Category, Blog, Comment
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from blog_app.forms import RegistrationForm


def home(request):
    featured_post = Blog.objects.filter(is_featured=True)  #.order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False)

    #   Fetch about us
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
    post = Blog.objects.filter(status='Published', category=category_id)

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
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    # Comment section setup
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        'comment_count': comment_count,
        'comments': comments,
        'single_blog': single_blog
    }
    return render(request, 'blogs.html', context)


# Search endpoint
def search(request):
    keyword = request.GET.get('keyword')
    blog_title = Blog.objects.filter(
        Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),
        status=1)
    context = {
        'blog': blog_title,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)


def Register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=True)
            form.save()
            send_mail(
                "Welcome to Django Blog",
                "Congratulations on creating your account",
                settings.DEFAULT_FROM_EMAIL,
                [current_user.email]
            )
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')
