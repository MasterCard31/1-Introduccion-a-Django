from django.urls import path

from . import views

urlpatterns = [
    # Suma: 
    path('/sumar/<int:num1>/<int:num2>/', views.sumar, name='sumar'),
    # Resta: 
    path('/restar/<int:num1>/<int:num2>/', views.restar, name='restar'),
    # Multiplicación: 
    path('/multiplicar/<int:num1>/<int:num2>/', views.multiplicar, name='multiplicar'),

]
