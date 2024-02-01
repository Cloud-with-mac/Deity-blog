from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "categories"


# TO CREATE A DROP-DOWN
STATUS_CHOICES = (
    ('Draft', 'Draft'),
    (1, 'Published'),
)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # the featured-image will be uploaded to a folder called upload with the current year, month and date
    feature_image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    short_description = models.TextField(max_length=1000)
    blog_body = models.TextField(max_length=2000)
    status = models.IntegerField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
