from django.db import models
from PIL import Image

DONOR_LEVELS = (
    ("P", "Platinum"),
    ("G", "Gold"),
    ("S", "Silver"),
    ("B", "Bronze"),
    ("I", "Individual"),
    ("O", "Other")
    )

# Create your models here.
class Donor(models.Model):
    """
    Model for Donors to DCPYthon.
    """
    name = models.CharField(max_length=100)
    url = models.URLField()
    slogan = models.CharField(max_length=200)
    level = models.CharField(max_length=1, choices=DONOR_LEVELS)
    logo = models.ImageField(upload_to="donor_logos")
