from django import forms
from .models import BugReport


class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['bug_url', 'description', 'instructions', 'occured']