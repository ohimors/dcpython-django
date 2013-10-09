# encoding: utf-8

from django.shortcuts import render
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DateDetailView

from .models import Event


def event_list(request):
    upcoming = Event.objects.upcoming()
    past = Event.objects.past()

    ctx = {"upcoming": upcoming,
           "past": past,
           # Used for navigation styling:
           "active": "events"}

    return render(request, 'events/event_list.html', ctx)


class EventYearArchiveView(YearArchiveView):
    queryset = Event.objects.all()
    date_field = "start_time"
    make_object_list = True
    allow_future = True


class EventMonthArchiveView(MonthArchiveView):
    queryset = Event.objects.all()
    date_field = "start_time"
    make_object_list = True
    allow_future = True


class EventDetail(DateDetailView):
    queryset = Event.objects.all()
    date_field = "start_time"
    month_format = '%m'
    allow_future = True
