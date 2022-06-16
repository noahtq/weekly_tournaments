from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from .models import Event


#Create new Mixin that checks if a user is staff
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


def home(request):
    context = {
        'event': Event.objects.all().first(),
        'events': Event.objects.all()
    }
    return render(request, 'events/home.html', context)


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    ordering = ['event_datetime']


class EventDetailView(DetailView):
    model = Event


class EventRegisterView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'events/event_register.html'
    fields = ['registered_users']
    # form_class = EventRegisterForm
    # success_url = '/'


class EventCreateView(StaffRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'type', 'description', 'location', 'event_datetime']   

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventUpdateView(StaffRequiredMixin, UpdateView):
    model = Event
    fields = ['title', 'type', 'description', 'location', 'event_datetime']   

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventDeleteView(StaffRequiredMixin, DeleteView):
    model = Event
    success_url = '/'


def about(request):
    return render(request, 'events/about.html', {'title': 'About'})
