from django import forms
from support.models import Donor, DONATION_TYPES

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        exclude = ["level", "secret"]

class DonationForm(forms.Form):
    donation_type = forms.ChoiceField(choices=DONATION_TYPES, widget=forms.HiddenInput)
    payment_token = forms.CharField(max_length=64)
    donation = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0, widget=forms.HiddenInput)