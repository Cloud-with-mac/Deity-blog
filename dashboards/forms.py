from django import forms
from blog_app.models import Category


class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
