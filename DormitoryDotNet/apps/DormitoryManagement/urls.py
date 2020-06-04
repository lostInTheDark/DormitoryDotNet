from  . import views
from django.urls import path

app_name = 'DormitoryManagement'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
    path('single_post/', views.single_post, name = 'single_post'),
    path('contact/', views.contact, name = 'contact'),
    path('map1/', views.map1, name='map1'),
    path('map2/', views.map2, name='map2'),
    path('map3/', views.map3, name='map3'),
    path('map4/', views.map4, name='map4'),
    path('map5/', views.map5, name='map5'),
]
