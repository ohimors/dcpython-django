from django.shortcuts import get_object_or_404, render
from django.conf import settings
from universalclient import Client

# Meetup API
meetup = Client("http://api.meetup.com").setArgs(params={"key": settings.MEETUP_API_KEY})
events = meetup._('2').events.setArgs(params={"group_urlname": "dcpython"})


def events(request):
    return render(request, 'events/events.html', {"active": "events"})

