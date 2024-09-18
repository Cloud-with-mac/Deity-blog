from .forms import AddUserForm, EditUserForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from blog_app.views import blogs
from .forms import AddCategory, BlogPostForm
from blog_app.models import Category, Blog
from django.template.defaultfilters import slugify


@login_required(login_url='login')
def dashboard(request):

    category_count = Category.objects.all().count
    blog_count = Blog.objects.all().count
    context = {
        'category_count': category_count,
        'blog_count': blog_count
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    form = AddCategory()
    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        context = {'form': form}
        return render(request, 'dashboard/add_category.html', context)


def edit_category(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    form = AddCategory(instance=cat)
    if request.method == 'POST':
        form = AddCategory(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        context = {'form': form, 'cat': cat}
        return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
    cat_del = Category.objects.get(pk=pk)
    cat_del.delete()
    return redirect('categories')


def posts(request):
    posts = Blog.objects.all()
    context = {'posts': posts}
    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            # print('==>', slugify(title) + '-'+str(post.id))
            post.slug = slugify(title) + '-'+str(post.id) # Using the ID generated from line 67 to get the slug
            post.save()
            return redirect('posts')
    form = BlogPostForm()
    context = {'form': form}
    return render(request, 'dashboard/add_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES,  instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'dashboard/edit_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')


def users(request):
    users = User.objects.all()
    context ={
        'users': users
    }
    return render(request, 'dashboard/users.html', context)

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = AddUserForm()
    context = {'form': form}
    return render(request, 'dashboard/add_user.html',context)

def edit_user(request, pk):
    user = get_object_or_404(User, id=pk)
    form = EditUserForm(instance=user)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {
        'form': form
    }
    return render(request, 'dashboard/edit_user.html', context)

def delete_user(request, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()
    return redirect('users')
