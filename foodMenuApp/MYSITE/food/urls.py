
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.itemsCBV.as_view(),name="items"),
    
    path('items/<int:item_id>/', views.item_detail,name="item_detail"),
    path('create/', views.CreateItem.as_view(),name="item_create"),
    path('items/update/<int:item_id>/', views.item_update,name="item_update"),
    path('items/update/<int:item_id>/', views.item_update,name="item_update"),
]
