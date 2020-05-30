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
