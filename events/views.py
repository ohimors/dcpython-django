from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from universalclient import Client

# Meetup API
meetup = Client("http://api.meetup.com").setArgs(params={"key": settings.MEETUP_API_KEY})

# Upcoming events
upcoming = meetup._('2').events.setArgs(params={"group_urlname": "dcpython"})
upcoming = upcoming.get()
upcoming = upcoming.json()
upcoming = upcoming.get('results')

# Past events
past = meetup._('2').events.setArgs(params={"group_urlname": "dcpython", "status": "past"})
past = past.get()
past = past.json()
past = past.get('results')
past.reverse()


@cache_page(3600)  # Cache API results for one hour
def events(request):
    return render(request, 'events/events.html', {"upcoming": upcoming, "past": past, "active": "events"}) # active needed for nav


def update(request):
    """
    Look up events that have changed on meetup.com and call Models API
    """
