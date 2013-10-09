# encoding: utf-8

from django.views.decorators.cache import cache_page
from django.shortcuts import render

from app.integration.meetup import get_upcoming_events, get_past_events


@cache_page(3600)  # Cache API results for one hour
def event_list(request):
    upcoming = get_upcoming_events()
    past = get_past_events()

    return render(request, 'events/events.html', {"upcoming": upcoming,
                                                  "past": past,
                                                  # Used for navigation styling:
                                                  "active": "events"})


def update(request):
    """
    Look up events that have changed on meetup.com and call Models API
    """
