from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.base, name='base'),
    path('', views.studregst, name='studregst'),
    path('', views.loginpage, name='loginpage'),
    

    
    


]