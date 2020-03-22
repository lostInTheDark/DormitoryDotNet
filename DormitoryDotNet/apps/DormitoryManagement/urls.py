from  . import views
from django.urls import path

app_name = 'DormitoryManagement'
urlpatterns = [
    path('', views.index, name = 'index'),
]
