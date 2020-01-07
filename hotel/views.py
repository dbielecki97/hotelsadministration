from django.views import generic

from .models import Hotel, Room, Opinion


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
    model = Opinion
    template_name = 'create_opinion.html'
    success_url = '/'
    fields = ('message',)
