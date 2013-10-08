# encoding: utf-8

import datetime

from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.conf import settings

from universalclient import Client

from app.integration.meetup import parse_datetime_ms

# Meetup API
meetup = Client("http://api.meetup.com").setArgs(params={"key": settings.MEETUP_API_KEY})

# Upcoming events
upcoming_q = meetup._('2').events.setArgs(params={"group_urlname": "dcpython"})

# Past events
past_q = meetup._('2').events.setArgs(params={"group_urlname": "dcpython", "status": "past"})


@cache_page(3600)  # Cache API results for one hour
def events(request):
    upcoming = upcoming_q.get().json().get('results')
    past = past_q.get().json().get('results')

    for i in upcoming + past:
        i['start_time'] = parse_datetime_ms(i['time'], i['utc_offset'])
        if 'duration' in i:
            i['end_time'] = i['start_time'] + datetime.timedelta(milliseconds=i['duration'])

    return render(request, 'events/events.html', {"upcoming": upcoming,
                                                  "past": past,
                                                  # Used for navigation styling:
                                                  "active": "events"})


def update(request):
    """
    Look up events that have changed on meetup.com and call Models API
    """
