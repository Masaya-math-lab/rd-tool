from django.urls import path
from . import views

app_name = 'to_data'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('shapeing/', views.ShapingView.as_view(), name='shaping'),
]