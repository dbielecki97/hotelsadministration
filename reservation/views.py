from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from catering.models import Catering
from hotel.models import Client
from service_request.models import ServiceRequest
from .forms import ReceiptForm
from .forms import ReservationForm
from .models import Reservation, Receipt


class NewReservation(generic.CreateView):
    form_class = ReservationForm
    template_name = 'reservation_new.html'
    success_url = '/reservation/my/'

    def get_form_kwargs(self):
        kwargs = super(NewReservation, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class ReservationList(generic.ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    ordering = ('start',)

    def get_queryset(self):
        return Reservation.objects.filter(client=Client.objects.get(user=self.request.user), isRegistered__exact=False)


class ReservationDetail(generic.DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ReservationDetail, self).get_context_data(**kwargs)
        if self.object.isRegistered:
            context['service_requests'] = ServiceRequest.objects.filter(
                client=Client.objects.get(user=self.request.user), reservation=self.object).order_by(
                '-date')
        return context


class PaymentMethodEdit(generic.UpdateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'payment_method_edit.html'

    def get_form_kwargs(self):
        kwargs = super(PaymentMethodEdit, self).get_form_kwargs()
        self.success_url = reverse_lazy('reservation registered detail',
                                        kwargs={'pk': self.kwargs['reservation_pk']})
        return kwargs


class RegisteredReservationList(generic.ListView):
    model = Reservation
    template_name = 'reservation_registered_list.html'
    ordering = ('start',)

    def get_queryset(self):
        return Reservation.objects.filter(client=Client.objects.get(user=self.request.user), isRegistered__exact=True,
                                          isCheckedOut__exact=False)


def register(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.isRegistered = True
    catering = Catering()
    catering.save()
    reservation.catering = catering
    reservation.save()
    return HttpResponseRedirect(reverse('reservation registered detail', kwargs={'pk': pk}))


def check_out(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.isCheckedOut = True
    hotel = reservation.room.hotel
    reservation.save()
    return HttpResponseRedirect(reverse('hotel opinion', kwargs={'pk': hotel.pk}))
