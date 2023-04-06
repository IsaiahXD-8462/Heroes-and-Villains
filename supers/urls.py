from django.urls import path
from . import views

urlpatterns = [
    path('supers/', views.supers_list)
]