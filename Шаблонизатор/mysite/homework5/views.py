from django.shortcuts import render

# Create your views here.

def wePhone(request):
    product_info = {
        "NAME": "wePhone",
        "REAL_COST": 999,
        "FAKE_COST": 1999,
        "DESCRIPTION": """Компания weInc. CO выпустила свой флагманский смартфон wePhone в 20ХХ году!
Опробуйте сегодня на weinc.co.fake"""
    }
    return render(request, "product.html", product_info)

def weWatch(request):
    product_info = {
        "NAME": "weWatch",
        "REAL_COST": 299,
        "FAKE_COST": 599,
        "DESCRIPTION": """Компания weInc. CO выпустила свои флагманские смарт-часы wePhone в 20ХХ году!
Опробуйте сегодня на weinc.co.fake"""
    }
    return render(request, "product.html", product_info)

def weHome(request):
    product_info = {
        "NAME": "weHome",
        "REAL_COST": 199999,
        "FAKE_COST": 99999999,
        "DESCRIPTION": """Компания weInc. CO открыла предзаказ weHome, умного дома с ИИ!
Подайте заявку сегодня на weinc.co.fake"""
    }
    return render(request, "product.html", product_info)