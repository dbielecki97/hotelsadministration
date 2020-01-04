# Create your views here.
from django.views import generic
from .models import Hotel, Room


class HotelList(generic.ListView):
    model = Hotel
    template_name = 'landing_page.html'


class HotelDetail(generic.DetailView):
    template_name = 'hotel_detail.html'
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_rooms_count'] = Room.objects.filter(hotel=self.object, isAvailable=True).count()
        return context


class HotelAvailableRooms(generic.TemplateView):
    template_name = 'available_rooms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['pk'])
        context['available_rooms'] = Room.objects.filter(hotel=self.kwargs['pk'], isAvailable=True)
        return context


class RoomDetail(generic.DetailView):
    model = Room
    template_name = 'room_detail.html'
