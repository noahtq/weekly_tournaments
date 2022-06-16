from django import forms

class EventRegisterForm(forms.Form):
    test = forms.CharField()

    # def addRegistartion(self):