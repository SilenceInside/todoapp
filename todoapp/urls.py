from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<str:id>/complete/', views.complete_task),
    path('<str:id>/delete/', views.delete_task),
]