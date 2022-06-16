from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event


#Create new Mixin that checks if a user is staff
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


class NotRegisteredMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        users_registered = Event.objects.filter(id=3).first().registered_users.all()
        not_registered = True
        for user in users_registered:
            if user.id == self.request.user.id:
                not_registered = False
        return not_registered

    

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


# class EventRegisterView(NotRegisteredMixin, UpdateView):
#     model = Event
#     template_name = 'events/event_register.html'
#     fields = ['registered_users']


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

def EventRegisterView(request):
    event_pk = 3
    if request.method == 'POST':
        user = request.user
        event = Event.objects.get(pk=event_pk)

        event.registered_users.add(user)

        messages.success(request, f'You have been registered for {event.title}')
        return redirect('/')

    return render(request, 'events/event_register.html')

