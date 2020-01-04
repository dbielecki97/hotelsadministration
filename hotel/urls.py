from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^rooms/(?P<pk>\d*)$', views.HotelAvailableRooms.as_view(), name='hotel rooms'),
    url(r'^detail/(?P<pk>\d*)$', views.HotelDetail.as_view(), name='hotel detail'),
    url(r'^room/(?P<pk>\d*)$', views.RoomDetail.as_view(), name='hotel room'),
    url(r'^$', views.HotelList.as_view(), name='hotel list'),

]
