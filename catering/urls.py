from django.conf.urls import url
from django.views.generic import RedirectView

from .views import FoodList, add_food_to_catering_order

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/')),
    url(r'^list/(?P<reservation_pk>\d*)/(?P<catering_pk>\d*)$', FoodList.as_view(), name='catering food list'),
    url(r'^add/(?P<reservation_pk>\d*)/(?P<catering_pk>\d*)/(?P<food_pk>\d*)/(?P<quantity>\d*)$',
        add_food_to_catering_order, name='catering add')
]
