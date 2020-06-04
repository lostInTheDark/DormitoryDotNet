from django.shortcuts import render

def index(request):
    return render(request, 'DormitoryManagement/index.html')

def blog(request):
    return render(request, 'DormitoryManagement/blog.html')

def about(request):
    return render(request, 'DormitoryManagement/about.html')

def contact(request):
    return render(request, 'DormitoryManagement/contact.html')

def single_post(request):
    return render(request, 'DormitoryManagement/blog-single-post.html')

def contact(request):
    return render(request, 'DormitoryManagement/contact.html')

def map2(request):
    return render(request, 'DormitoryManagement/map2.html')

def map3(request):
    return render(request, 'DormitoryManagement/map3.html')

def map4(request):
    return render(request, 'DormitoryManagement/map4.html')

def map5(request):
    return render(request, 'DormitoryManagement/map5.html')

def map1(request):
    return render(request, 'DormitoryManagement/map1.html')
