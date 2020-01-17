from django.views import generic

from .forms import CreateOpinionForm
from .models import Hotel, Room


class HotelList(generic.ListView):
    model = Hotel
    template_name = 'landing_page.html'


class HotelDetail(generic.DetailView):
    template_name = 'hotel_detail.html'
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_rooms_count'] = Room.objects.filter(hotel=context['hotel']).count()
        context['available_rooms'] = Room.objects.filter(hotel=context['hotel'])
        return context


class RoomDetail(generic.DetailView):
    model = Room
    template_name = 'room_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RoomDetail, self).get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['hotel_pk'])
        return context


class CreateOpinion(generic.CreateView):
    template_name = 'create_opinion.html'
    form_class = CreateOpinionForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(CreateOpinion, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs
