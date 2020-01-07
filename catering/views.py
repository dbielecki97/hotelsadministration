from django.http import HttpResponseRedirect
from django.urls import reverse
from django_filters.views import FilterView

from catering.filters import FoodListFilter
from catering.models import Food, Catering
from reservation.models import Reservation


class FoodList(FilterView):
    filterset_class = FoodListFilter
    model = Food
    template_name = 'food_list.html'

    def get_context_data(self, **kwargs):
        context = super(FoodList, self).get_context_data(**kwargs)
        context['catering_pk'] = self.kwargs['catering_pk']
        context['reservation'] = Reservation.objects.get(pk=self.kwargs['reservation_pk'])
        return context


def add_food_to_catering_order(request, reservation_pk, catering_pk, food_pk, quantity):
    food_item, created = Catering.objects.get(pk=catering_pk).foodquantity_set.get_or_create(
        foodItem=Food.objects.get(pk=food_pk))
    food_item.quantity = food_item.quantity + int(quantity) if food_item.quantity is not None else 1
    food_item.save()

    Reservation.objects.get(pk=reservation_pk).receipt.update_costs()

    return HttpResponseRedirect(
        reverse('catering food list', kwargs=
        {
            'reservation_pk': reservation_pk,
            'catering_pk': catering_pk
        }))
