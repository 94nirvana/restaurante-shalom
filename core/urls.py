from django.urls import path
from .views import index, fila, transferencia
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='index'),
    path('fila/', fila, name='fila'),
    path('transferencia/', transferencia, name='transferencia'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

