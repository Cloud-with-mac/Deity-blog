from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:category_id>/', views.post_by_category, name='post_by_category'),
    path('', views.home, name='home'),
    # Register
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),
]