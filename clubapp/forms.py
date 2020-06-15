from django import forms
from .models import Meetings

class AddMeetingForm(forms.ModelForm):
    class Meta:
        model = Meetings
        fields = '__all__'

