from django.shortcuts import render
from django.views import generic
from .forms import ReservationForm
from django.urls import reverse_lazy


def home(request):
    return render(request, 'reservation_home.html')


class NewReservation(generic.FormView):
    template_name = 'reservation_new.html'
    form_class = ReservationForm
    success_url = reverse_lazy('hotel list')

    def get_form_kwargs(self):
        kwargs = super(NewReservation, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        kwargs['user'] = self.request.user
        return kwargs
