from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    category_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "categories"


STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published"),
)

class Blog(models.Model):

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    feature_image = models.ImageField(upload_to='upload/%Y/%M/%D/')
    short_description = models.TextField(max_length=5000)
    blog_body = models.TextField(max_length=10000, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    is_featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.comment

