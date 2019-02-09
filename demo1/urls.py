from django.conf.urls import url
from . import chanti
urlpatterns = \
[
    url(r'^$', chanti.wish),
    url(r'm1/', chanti.wish1),
    url(r'm2/', chanti.wish2),
]
