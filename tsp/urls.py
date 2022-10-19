from django.urls import path
from . import views

app_name = 'tsp'

urlpatterns = [
    path('', views.TitleView.as_view(), name='title'),
]