from django.urls import path
from . import views

app_name = 'to_data'
urlpatterns = [
    path('', views.index, name='index'),
    path('/help', views.help, name='help'),
]