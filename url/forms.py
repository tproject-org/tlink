from django import forms
from .models import URL 

class UrlForm(forms.ModelForm): 
    class Meta: 

        model = URL 
        fields = ['url', 'short_url']