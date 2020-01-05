from django.shortcuts import render
from django.views import generic

from service_request.forms import NewServiceRequestForm


def home(request):
    return render(request, 'service_request-home.html')


class NewServiceRequest(generic.CreateView):
    form_class = NewServiceRequestForm
    template_name = 'service_request_create.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(NewServiceRequest, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        kwargs['user'] = self.request.user
        self.success_url = '/reservation/my/{}'.format(self.kwargs['pk'])
        return kwargs
