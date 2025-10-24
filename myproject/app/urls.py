from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('log_in/', views.log_in, name='log_in'),
   path('inside/', views.inside, name='inside'),
   path('order/', views.order, name='order'),
   path('showproduct/', views.showproduct, name='showproduct'),
   path('view/', views.view, name='view'),
   
]