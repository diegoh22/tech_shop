from django.urls import path
from .views import item_list

app_name = 'tech_shop'

urlpatterns = [
    path(''. item_list, name='item-list')
]