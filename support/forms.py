from django.forms import ModelForm
from support.models import Donor

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        exclude = ["level", "secret"]
