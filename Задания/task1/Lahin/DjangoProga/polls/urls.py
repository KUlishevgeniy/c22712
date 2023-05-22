from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('html', views.html, name='html'),
    path('newpage', views.newpage, name='newpage')
]