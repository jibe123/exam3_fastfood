from django.urls import path
from .views import main_page, menu_detail_view

urlpatterns = [
    path('', main_page),
    path('menu/<int:id>/', menu_detail_view),
]