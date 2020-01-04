from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/(?P<pk>\d*)$', views.NewReservation.as_view(), name='reservation new'),
    url(r'', views.home, name='reservation'), ]
