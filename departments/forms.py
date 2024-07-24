# forms.py
from django import forms
from django.urls import reverse
from .models import *

class ICTForm(forms.ModelForm):
    class Meta:
        model = ICT
        fields = '__all__'



class QHSEVideoForm(forms.ModelForm):
    class Meta:
        model = QHSEVideo
        fields = "__all__"
