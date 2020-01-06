from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^new/(?P<pk>\d*)$', views.NewServiceRequest.as_view(), name='service request new'),
    url(r'^$', RedirectView.as_view(url='/')),
]
