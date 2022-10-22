from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('tsp/', include('tsp.urls')),
    path('tsp/', include('tsp.urls')),

    path('', include('tsp.urls')),
    path('posting', include('posting.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)