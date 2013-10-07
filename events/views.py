from django.shortcuts import get_object_or_404, render
from django.conf import settings
from universalclient import Client

# Meetup API
meetup = Client("http://api.meetup.com").setArgs(params={"key": settings.MEETUP_API_KEY})
events = meetup._('2').events.setArgs(params={"group_urlname": "dcpython"})
upcoming = events.get()
upcoming = upcoming.json()
upcoming = upcoming['results']


def events(request):
    return render(request, 'events/events.html', {"upcoming": upcoming})


def update(request):
    """
    Look up events that have changed on meetup.com and call Models API
    """
