from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, '../templates/home.html')

def base(request):
    return render(request, '../templates/base.html')

def studregst(request):
    return render(request, '../templates/studregst.html')

def loginpage(request):
    return render(request, '../templates/loginpage.html')        



