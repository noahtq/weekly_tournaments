from django.shortcuts import render
from django.contrib import messages


def submitReport(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Your bug report was submitted successfully!')
            return redirect('events-home')
