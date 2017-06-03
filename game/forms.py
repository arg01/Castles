from django import forms
from .models import players


class playersForm(forms.ModelForm):

    class Meta:
        model = players
        fields= ('name','Allocations1','Allocations2', 'Allocations3', 'Allocations4', 'Allocations5', 'Allocations6', 'Allocations7','Allocations8', 'Allocations9', 'Allocations10')
