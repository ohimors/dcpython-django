from django.shortcuts import get_object_or_404, render
from support.forms import DonorForm, DonationForm
from support.models import Donor
from django.template import RequestContext
from django.conf import settings
# Create your views here.

def support(request):
    context = RequestContext(request)
    context.update({"active": "donate", "donor_form": DonorForm(), "donation_form": DonationForm, "balanced_uri": settings.BALANCED_URI })
    return render(request, 'support/support.html', context)

def donor_update(request, secret=None):
    donor = get_object_or_404(Donor, secret=secret)
    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
    else:
        form = DonorForm(instance=donor)
    context = RequestContext(request)
    context.update({"secret": secret, "form": form, "name": donor.name})
    return render(request, 'support/donor_update.html', context)
