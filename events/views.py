from django.shortcuts import render
# from .models import Event


def home(request):
    context = {
        # 'events': Event.objects.all()
    }
    return render(request, 'events/home.html', context)


def about(request):
    return render(request, 'events/about.html', {'title': 'About'})

