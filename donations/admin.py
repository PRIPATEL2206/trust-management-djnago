from django.contrib import admin
from .models import DonationType,Donation
# Register your models here.

class AdminDonationType(admin.ModelAdmin):
    list_display=['id','name','created_by','starting_date','ending_date','is_forever']


class AdminDonation(admin.ModelAdmin):
    list_display=['id','add_by','donation_for','display_name','handover_by','desc','amount']

admin.site.register(DonationType,AdminDonationType)
admin.site.register(Donation,AdminDonation)