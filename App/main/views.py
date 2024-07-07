from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }

    return render(request, 'main/about.html', context)

def info(request):
    context = {
        'title': 'Home - О нас',
        'content': "Контактная информация:",
        'text_on_page': "г.Оренбург, ул.Чкалова, д.9 инд:460000 тел.: 9292522270"
    }

    return render(request, 'main/info.html', context)

def delivery(request):
    context = {
        'title': 'Home - О нас',
        'content': "Доставка и оплата:",
        'text_on_page': "Информацию о способах и стоимости доставки уточняйте по телефону +79292522270, оплата осуществляется в магазине."
    }

    return render(request, 'main/delivery.html', context)