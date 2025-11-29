"""
- import ModelForm
- import the Model
- create ModelForm instance
"""

from django.forms import ModelForm
from .models import Shoe

class shoeForm(ModelForm):
    class Meta: 
        model = Shoe
        fields = '__all__'