from django.urls import path
from . import views

app_name = 'tsp'

urlpatterns = [
    path('', views.TitleView.as_view(), name='title'),
    path("ajax/", views.call_write_data, name="call_write_data"),
    path('create_city_page/', views.CreateCityView.as_view(), name='create_city_page'),
    path('create_city/', views.create_city, name='create_city'),
    path('search/', views.search, name='search')
]