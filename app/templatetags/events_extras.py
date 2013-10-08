from dateutil.tz import tzutc
from dateutil.tz import tzoffset
from django import template

import datetime

register = template.Library()


# Via https://github.com/pythonkc/pythonkc-meetups/blob/master/pythonkc_meetups/parsers.py#L102
def parse_datetime(utc_timestamp_ms, utc_offset_ms):
    """
    Create a timezone-aware ``datetime.datetime`` from the given UTC timestamp
    (in milliseconds), if provided. If an offest it given, it is applied to the
    datetime returned.

    Parameters
    ----------
    utc_timestamp_ms
        UTC timestamp in milliseconds.
    utc_offset_ms
        Offset from UTC, in milliseconds, to apply to the time.

    Returns
    -------
    A ``datetime.datetime`` if a timestamp is given, otherwise ``None``.

    """
    if utc_timestamp_ms:
        utc_timestamp_s = utc_timestamp_ms / 1000
        dt = datetime.datetime.fromtimestamp(utc_timestamp_s, tzutc())

        if utc_offset_ms:
            utc_offset_s = utc_offset_ms / 1000
            dt + datetime.timedelta(seconds=utc_offset_s)

        return dt


def convert_seconds_to_datetime(event):
    """
    Meetup gives us seconds, we need a Python datetime object
    """

    return parse_datetime(event['time'], 0)


register.filter('convert_seconds_to_datetime', convert_seconds_to_datetime)
