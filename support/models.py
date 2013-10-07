from django.db import models
from PIL import Image
import base64
import os

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
    url = models.URLField(blank=True, null=True)
    slogan = models.CharField(max_length=200, blank=True, null=True)
    level = models.CharField(max_length=1, choices=DONOR_LEVELS, blank=True, null=True)
    logo = models.ImageField(upload_to="donor_logos", blank=True, null=True)
    secret = models.CharField(max_length=90)

    def save (self, *args, **kwargs):
        if not self.secret:
            self.secret = base64.urlsafe_b64encode(os.urandom(64))
        super(Donor, self).save(*args, **kwargs)
