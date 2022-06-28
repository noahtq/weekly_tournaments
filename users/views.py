from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UpdateTeammatesForm
from events.models import Event
from users.models import User


def getUserEvents(user):
    all_events = Event.objects.all()
    registered_events = []
    for event in all_events:
        event_users = event.registered_users.all()
        if user in event_users:
            registered_events.append(event)
    return registered_events


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):

    registered_events = getUserEvents(request.user)
    teammates = request.user.profile.favorite_teammates.all()
    
    context = {
        'events': registered_events,
        'teammates': teammates
    }

    return render(request, 'users/profile.html', context)


@login_required
def profileUpdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update_profile.html', context)


@login_required
def teammatesUpdate(request):
    users = User.objects.all()
    current_teammates = request.user.profile.favorite_teammates.all()
    current_teammates_id = []
    for teammate in current_teammates:
        current_teammates_id.append(teammate.id)
    if request.method == 'POST':
        data = request.POST
        request.user.profile.favorite_teammates.clear()
        new_teammates = []
        for k in data.keys():
            if 'user_id' in k:
                teammate_id = int(k.split('user_id_')[1])
                teammate = User.objects.filter(id=teammate_id).first()
                new_teammates.append(teammate)
                request.user.profile.favorite_teammates.add(teammate)
        messages.success(request, f'Teammates have been updated')
        return redirect('profile')
    
    context = {
        'users': users,
        'myuser': request.user,
        'current_teammates_id': current_teammates_id
    }
    return render(request, 'users/teammates_update.html', context)
