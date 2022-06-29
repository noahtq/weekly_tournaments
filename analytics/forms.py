from django import forms
from .models import BugReport
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
import re


class BugReportForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        bug_url = self.cleaned_data['bug_url']
        occured = self.cleaned_data['occured']

        #Check that url comes from one of our allowed hosts
        allowed_hosts = settings.ALLOWED_HOSTS
        host_patterns = []
        for host in allowed_hosts:
            host_patterns.append(f'[/.]*{host}[:.]*')
        match = False
        for pattern in host_patterns:
            if re.search(pattern, bug_url):
                match = True
        if match == False:
            raise forms.ValidationError('The url must be from this website')
        
        #Check that the datetime is sometime in the past
        if occured > timezone.now():
            raise forms.ValidationError('The occured time can not be in the future')

        return cleaned_data

    class Meta:
        model = BugReport
        fields = ['bug_url', 'description', 'instructions', 'occured']
        labels = {
            'bug_url': _('URL of page where bug occured'),
            'description': _('Describe what went wrong'),
            'instructions': _('Explain how to recreate the error (what were you doing before the error occured)'),
            'occured': _('Time and date of error'),
        }