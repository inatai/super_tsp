from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tsp/', include('tsp.urls')),
    path('admin/', admin.site.urls),
]