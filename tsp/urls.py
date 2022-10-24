from django.urls import path
from . import views

app_name = 'tsp'

urlpatterns = [
    path('', views.TitleView.as_view(), name='title'),
    path("ajax/", views.call_write_data, name="call_write_data"),
]