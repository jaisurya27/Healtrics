from django.db import models
import django
import uuid
# Create your models here.
from accounts.models import *
from admin_app.models import *

class BloodBankProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    blood_bank_name = models.TextField()
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    contact_email = models.EmailField(max_length=255)
    contact_number = models.TextField()
    website_url = models.URLField(max_length=255, null=True)
    logo = models.ImageField(upload_to='images/', null=True)
    bloodbank_operating_license_certificate = models.FileField(upload_to='certs/')
    certificate_of_accreditation = models.FileField(upload_to='certs/')

class BloodCamp(models.Model):
    blood_bank = models.ForeignKey(BloodBankProfile,on_delete=models.CASCADE)
    camp_id = models.UUIDField(default=uuid.uuid4, editable=False)
    camp_name = models.TextField()
    camp_date = models.DateField()
    camp_time = models.TimeField()
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    contact_email = models.EmailField(max_length=255)
    contact_number = models.TextField()
    team_size = models.IntegerField()
    camp_brochure = models.FileField(upload_to='camps/', null=True)
    camp_status = models.CharField(max_length=50)







