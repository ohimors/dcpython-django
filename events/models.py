# encoding: utf-8
from __future__ import absolute_import

from itertools import chain

from django.db import models

from app.integration.meetup import get_upcoming_events, get_past_events


class Venue(models.Model):
    meetup_id = models.CharField(unique=True, max_length=32)

    # TODO: switch to GeoDjango PointField?
    lon = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6)

    name = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, blank=True)
    address_3 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5, blank=True)

    repinned = models.BooleanField()

    @classmethod
    def create_from_meetup(cls, meetup_data):
        i, created = cls.objects.get_or_create(meetup_id=meetup_data['id'])

        for k, v in meetup_data.items():
            if k == "id": continue
            setattr(i, k, v)

        i.full_clean()
        i.save()
        return i


class Event(models.Model):
    record_created = models.DateTimeField(auto_now_add=True)
    record_modified = models.DateTimeField(auto_now=True)

    meetup_id = models.CharField(unique=True, max_length=32)

    name = models.CharField(max_length=200)
    venue = models.ForeignKey("Venue", null=True, blank=True)

    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True, blank=True)

    meetup_url = models.URLField(blank=True)

    description = models.TextField(blank=True, null=True)

    @classmethod
    def sync_from_meetup(cls):
        for i in chain(get_past_events(), get_upcoming_events()):
            event, created = cls.objects.get_or_create(meetup_id=i['id'])

            for j in ('name', 'description', 'start_time', 'end_time'):
                setattr(event, j, i.get(j))

            event.meetup_url = i['event_url']

            venue = i.get('venue')
            if venue:
                event.venue = Venue.create_from_meetup(venue)

            event.full_clean()
            event.save()
