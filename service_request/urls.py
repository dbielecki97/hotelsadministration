from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^new/(?P<pk>\d*)$', views.NewServiceRequest.as_view(), name='service request new'),
    url(r'^$', views.home, name='home'),
]
