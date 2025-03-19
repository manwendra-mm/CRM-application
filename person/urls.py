from django.urls import path

from . import views

urlpatterns=[
    path('registration/', views.registerPage, name='registration'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    
    path('',views.dashboard,name='dashboard'),
    path('product/', views.pro, name='product'),
    path('create_order/', views.createorder, name='create_order'),
    path('update_order/<str:pk>/', views.updateorder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteorder, name='delete_order'),
    path('customer/<str:pk_test>/', views.cus, name='customer')
]