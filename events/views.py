from django.shortcuts import get_object_or_404, render
# Create your views here.

def events(request):
    return render(request, 'events/events.html', {"active": "events"})