from django import forms
from .models import EventVideo, Event




class EventVideoAdminForm(forms.ModelForm):
    class Meta:
        model = EventVideo
        fields = '__all__'
