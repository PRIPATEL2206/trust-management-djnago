from django import forms
from .models import Donation,DonationType
from datetime import datetime

class AddDonationTypeForm(forms.ModelForm):
    ending_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','value':datetime.now()}))

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():            
            match visible.name:
                case 'desc':
                    visible.field.widget.attrs['rows'] = 3

    class Meta:
        model = DonationType
        fields=('__all__')

class AddDonationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():            
            match visible.name:
                case 'desc':
                    visible.field.widget.attrs['rows'] = 3

    class Meta:
        model = Donation
        fields=('__all__')

        