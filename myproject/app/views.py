from django.shortcuts import render
from django.urls import path

# Create your views here.
def log_in(request):
  return render(request, 'log_in.html')

def inside(request):
  return render(request, 'inside.html')

def order(request):
  return render(request, 'order.html')

def showproduct(request):
  return render(request, 'showproduct.html')

def home(request):
  return render(request, 'home.html')

def view(request):
  return render(request, 'view.html')


urlpatterns = [
  
  path('log_in/', log_in, name='log_in'),
  path('inside/', inside, name='inside'),
  path('order/', order, name= 'order'),
  path('showproduct/', showproduct, name= 'showproduct'),
  path('view/', view, name='view'),
]

   


    
    
