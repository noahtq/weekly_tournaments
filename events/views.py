from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event


#Check if user is already registered for event, return boolean value
def checkRegistration(user, event):
    user_id = user.id
    registered_users = event.registered_users.all()

    for r_user in registered_users:
        if r_user.id == user_id:
            return True
    return False

#Check if there is still room in the tournament
def checkEventFilled(event):
    spots = event.max_users
    taken = event.registered_users.all().count()
    if taken >= spots:
        return True
    return False

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


    def get_context_data(self, *args, **kwargs):
        path = self.request.path
        event_pk = int(path.split('event/')[1].split('/')[0])
        event = Event.objects.get(pk=event_pk)
        user = self.request.user
        registered = checkRegistration(user, event)
        is_filled = checkEventFilled(event)
        
        context = super(EventDetailView, self).get_context_data(*args, **kwargs)
        context['registered'] = registered
        context['is_filled'] = is_filled
        return context


class EventCreateView(StaffRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'type', 'description', 'location', 'event_datetime', 'price', 'max_users']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventUpdateView(StaffRequiredMixin, UpdateView):
    model = Event
    fields = ['title', 'type', 'description', 'location', 'event_datetime', 'price', 'max_users']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventDeleteView(StaffRequiredMixin, DeleteView):
    model = Event
    success_url = '/'


def about(request):
    return render(request, 'events/about.html', {'title': 'About'})


@login_required
def EventRegisterView(request):
    event_pk = request.GET.get('event')
    event = Event.objects.get(pk=event_pk)
    user = request.user

    isRegistered = checkRegistration(user, event)
    isFilled = checkEventFilled(event)
    
    if request.method == 'POST' and isFilled == False and isRegistered == False:

        event.registered_users.add(user)

        messages.success(request, f'You have been registered for {event.title}')
        return redirect('event-register-success')

    context = {
        'event': event,
        'registered': isRegistered,
        'client_id': settings.PAYPAL_CLIENT_ID,
        'is_filled': isFilled,
        'adult_only': True #replace this in future version to add adult only and age defined in event model
    }

    return render(request, 'events/event_register.html', context)


def eventSuccessView(request):
    return render(request, 'events/event_register_success.html')

