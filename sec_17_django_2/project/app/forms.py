from django import forms

from app.models import User

class NewUserForm(forms.ModelForm):
    # add custom validators here
    class Meta:
        model = User # link to model
        fields = '__all__'