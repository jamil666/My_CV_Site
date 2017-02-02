from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from cv_site import views


urlpatterns = [

        url(r'^$', views.home, name='home'),
        url(r'^contact', views.contact, name='contact'),
        url(r'^send_mail', views.send_mail, name='send_mail'),
        url(r'^error', views.error, name='error'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

