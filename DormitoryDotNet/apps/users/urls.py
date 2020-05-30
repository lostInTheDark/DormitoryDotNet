from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('single_post/', views.single_post, name = 'single_post')
]
