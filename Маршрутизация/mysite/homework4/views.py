from random import choice
from django.shortcuts import render, HttpResponse

# Create your views here.


def pages_1_random():
    random_list_1 = [
        "Привет!",
        "Как дела?"
    ]

    return HttpResponse(choice(random_list_1))


def pages_2_random():
    random_list_1 = [
        "Пока!",
        "Давай потом поболтаем?"
    ]

    return HttpResponse(choice(random_list_1))


def pages_page1(request):
    return pages_1_random()


def pages_page2(request):
    return pages_2_random()