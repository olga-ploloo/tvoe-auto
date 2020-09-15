
from django.conf import settings
from django.urls import path
from avto import views

from django.conf.urls.static import static

from avto.views import Start

urlpatterns = [
    path('',  Start.as_view(), name='start'),
           ]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)