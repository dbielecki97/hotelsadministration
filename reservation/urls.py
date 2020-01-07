from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^new/(?P<pk>\d*)$', views.NewReservation.as_view(), name='reservation new'),
    url(r'^my/(?P<reservation_pk>\d*)/receipt/(?P<pk>\d*)/paymentmethod$', views.PaymentMethodEdit.as_view(),
        name='receipt edit'),
    url(r'^my/register/(?P<pk>\d*)$', views.register, name='reservation register'),
    url(r'^my/registered/(?P<pk>\d*)$', views.ReservationDetail.as_view(), name='reservation registered detail'),
    url(r'^my/registered/$', views.RegisteredReservationList.as_view(), name='reservation registered list'),
    url(r'^my/(?P<pk>\d*)$', views.ReservationDetail.as_view(), name='reservation detail'),
    url(r'^my/$', views.ReservationList.as_view(), name='reservation list'),
    url(r'^(?P<pk>\d*)/checkout$', views.check_out, name='reservation checkout'),
    url(r'^$', RedirectView.as_view(url='/')),
]
