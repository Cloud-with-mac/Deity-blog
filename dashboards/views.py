from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from .forms import AddCategory

from blog_app.models import Category, Blog

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
