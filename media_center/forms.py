from django import forms
from .models import EventVideo, Event




class EventVideoAdminForm(forms.ModelForm):
    class Meta:
        model = EventVideo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['related_event'].widget = forms.Select(choices=Event.objects.all().values_list('name'))
