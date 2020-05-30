from  . import views
from django.urls import path

app_name = 'DormitoryManagement'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
    path('single_post/', views.single_post, name = 'single_post'),
]
