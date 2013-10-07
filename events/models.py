from django.db import models

# Create your models here.

class Venue(models.Model):
	meetup_id = models.IntegerField()
	zip_code = models.CharField(max_length=5)
	lon = models.IntegerField()
	lat = models.IntegerField()
	repinned = models.BooleanField()
	name = models.CharField(max_length=200)
	state = models.CharField(max_length=2)
	address_1 = models.CharField(max_length=200)
	address_2 = models.CharField(max_length=200)
	address_3 = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	country=models.CharField(max_length=2)



class Event(models.Model):
	meetup_id = models.IntegerField()
	utc_offset = models.IntegerField()
	duration = models.IntegerField()
	time = models.DateTimeField()
	last_updated = models.DateTimeField()
	created = models.DateTimeField()
	meetup_url = models.URLField()
	description = models.TextField()
	name = models.CharField(max_length=200)
	venue = models.ForeignKey("Venue")
