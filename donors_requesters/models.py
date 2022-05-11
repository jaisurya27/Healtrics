from django.db import models
import django
import uuid
# Create your models here.
from accounts.models import *
from blood_banks.models import *
from hospitals.models import *


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.TextField()
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    blood_group = models.CharField(max_length=10)
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    aadhar_number = models.TextField(unique=True) 
    contact_email = models.EmailField(max_length=255)
    contact_number = models.Textfield(max_length=255)
    profile_pic = models.ImageField(upload_to='images/',null=True)
    last_donation_date = models.DateField()
    coins_earned = models.IntegerField(default=0)

class ParticipateCamp(models.Model):
    blood_camp = models.ForeignKey(BloodCamp, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type_of_donation = models.CharField(max_length=255,null=True)
    blood_group = models.CharField(max_length=10, null=True)
    blood_collected_date_time = models.DateTimeField(null=True)
    quantity = models.IntegerField(null=True)
    expiry_date = models.DateField(null=True)

class BloodRequest(models.Model):
    requester_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hospital_profile = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    request_id = models.UUIDField(default=uuid.uuid4, editable=False)
    request_date_time = models.DateTimeField(default = django.utils.timezone.now)
    request_duration = models.FloatField()
    blood_type_needed  = models.CharField(null=False)
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    contact_email = models.EmailField(max_length=255)
    contact_number = models.TextField(null=False)
    status = models.CharField(max_length=50,default='request_added')

class BloodRequestDonor(models.Model):
    blood_request = models.ForeignKey(BloodRequest, on_delete=models.CASCADE)
    donor_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    accepted_date_time = models.DateTimeField(default = django.utils.timezone.now)
    donor_availability = models.FloatField()
    donor_distance = models.FloatField()
    contact_email = models.EmailField(max_length=255)
    contact_number = models.TextField()
    is_request_satisfied = models.BooleanField()






