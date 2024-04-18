from random import randint
from django.shortcuts import render, HttpResponse

# Create your views here.


def game(request):
    numbers = []
    for number in range(3):
        numbers.append(randint(1,3))

    if len(set(numbers)) == 3:
        return HttpResponse("Победа, все 3 числа равны!")

    return HttpResponse("Повезет в следующий раз!")