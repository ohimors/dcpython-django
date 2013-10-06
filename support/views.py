from django.shortcuts import get_object_or_404, render
# Create your views here.

def support(request):
    return render(request, 'support/support.html', {"active": "support"})