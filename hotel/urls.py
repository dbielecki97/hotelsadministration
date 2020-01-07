from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detail/(?P<pk>\d*)$', views.HotelDetail.as_view(), name='hotel detail'),
    url(r'^detail/(?P<hotel_pk>\d*)/room/(?P<pk>\d*)$', views.RoomDetail.as_view(), name='hotel room'),
    url(r'^(?P<pk>\d*)/opinion$', views.CreateOpinion.as_view(), name='hotel opinion'),
    url(r'^$', views.HotelList.as_view(), name='hotel list'),
]
