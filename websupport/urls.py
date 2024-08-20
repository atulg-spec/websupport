from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from home.views import error_404_view, error_500_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('', include('home.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = error_404_view
handler500 = error_500_view

