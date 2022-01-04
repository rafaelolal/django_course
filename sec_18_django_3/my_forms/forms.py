from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean = super().clean()
        email = all_clean['email']
        verify = all_clean['verify_email']

        if email != verify:
            raise forms.ValidationError('MAKE SURE EMAILS MATCH!')