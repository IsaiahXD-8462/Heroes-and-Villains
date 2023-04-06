from django.urls import path
from . import views

urlpatterns = [
    path('super_types/', views.super_types_list)
]