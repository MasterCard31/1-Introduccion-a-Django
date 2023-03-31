from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Desde la visa de encuestas!")

def sumar(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse('El suma de %i + %i = %i' % (num1, num2, resultado))

def restar(request, num1, num2):
    resultado = num1 - num2
    return HttpResponse('El resta de %i - %i = %i' % (num1, num2, resultado))

def multiplicar(request, num1, num2):
    resultado = num1 * num2
    return HttpResponse('El multiplicación de %i x %i = %i' % (num1, num2, resultado))
