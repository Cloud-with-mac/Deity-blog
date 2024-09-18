from django.contrib.messages import success
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('category/<int:category_id>/', views.post_by_category, name='post_by_category'),
    path('', views.home, name='home'),
    # Register
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),

    # Password Management
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset.html'), name='reset_password'),
    # show a success message stating that an email was sent to reset our password
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_sent.html'), name='password_reset_done'),
    # send a link to our email, so that we can reset our password
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_form.html'), name='password_reset_confirm'),
    # show a success message that our password was changed
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),
]