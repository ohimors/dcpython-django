from django.contrib import admin
from support.models import Donor

class DonorAdmin(admin.ModelAdmin):
    readonly_fields = ("secret",)

admin.site.register(Donor, DonorAdmin)