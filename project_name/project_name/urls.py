from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/docs/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
