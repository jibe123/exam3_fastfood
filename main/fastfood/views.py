from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from django.http import Http404
# Create your views here.


def main_page(request):
    all_items_from_menu = Menu.objects.all()
    context = {"menu_all": all_items_from_menu}
    return render(request, 'menu/main.html', context=context)


def menu_detail_view(request, id=None):
    menu_object = None
    print(id)
    if id is not None:
        try:
            menu_object = Menu.objects.get(id=id)
        except:
            raise Http404
    context = {
        "menu_object": menu_object
    }
    return render(request, "menu/menu_detail.html", context=context)

