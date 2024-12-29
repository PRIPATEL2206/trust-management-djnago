from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class DonationType(models.Model):
    name = models.CharField(max_length=100,null=False)
    desc = models.TextField(blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='donation_types',null=False,editable=False)
    photo = models.ImageField(upload_to='donation_types/',null=False,default='donation_types/defult_donationtype.png')
    is_forever = models.BooleanField(default=False)
    starting_date  = models.DateTimeField(auto_now_add=True)
    ending_date  = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name + " - " + self.desc[:10]
    

class Donation(models.Model):
    add_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='donations',null=False,editable=False)
    donation_for = models.ForeignKey('DonationType',on_delete=models.CASCADE,related_name='donations',null=False)
    amount = models.PositiveIntegerField(null=False)
    display_name = models.CharField(max_length=100,null=False)
    handover_by = models.CharField(max_length=100,null=False)
    desc = models.TextField(blank=True)   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name