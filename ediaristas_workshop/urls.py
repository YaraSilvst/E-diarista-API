from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from web.views import listar_diaristas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('', listar_diaristas, name = "listar_diarista"),
    path('api/', include('api.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
