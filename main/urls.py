from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('tip/', views.tip, name = 'tip'),
    path('display/', views.display, name = 'display'),
]