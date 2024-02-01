from django.contrib import admin
from .models import Category, Blog


# Generating slug title for our blog
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'is_featured', 'status')
    search_fields = ('title', 'category__category_name', 'status')
    list_editable = ('is_featured',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
