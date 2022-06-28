from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BugReportForm


def submitReport(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your bug report was submitted successfully!')
            return redirect('events-home')
    else:
        form = BugReportForm()
    prev_url = request.META.get('HTTP_REFERER', '')

    context = {
        'form': form,
        'prev_url': prev_url
    }
    return render(request, 'analytics/bug_report.html', context)
