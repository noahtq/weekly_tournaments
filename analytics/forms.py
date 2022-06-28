from django import forms
from .models import BugReport
from django.utils.translation import gettext_lazy as _


class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['bug_url', 'description', 'instructions', 'occured']
        labels = {
            'bug_url': _('URL of page where bug occured'),
            'description': _('Describe what went wrong'),
            'instructions': _('Explain how to recreate the error (what were you doing before the error occured)'),
            'occured': _('Time and date of error'),
        }