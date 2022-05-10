from django.db import models
import django
# Create your models here.
from accounts.models import *
from admin_app.models import *

class HospitalProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hospital_name = models.TextField()
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    contact_email = models.EmailField(max_length=255)
    contact_number = models.TextField()
    website_url = models.URLField(max_length=255, null=True)
    logo = models.ImageField(upload_to='images/')
    clinic_establishment_certificate = models.FileField(upload_to='certs/')
    companies_registration_act_certificate = models.FileField(upload_to='certs/')
    societies_registration_act_certificate = models.FileField(upload_to='certs/')
    bloodbank_operating_license_certificate = models.FileField(upload_to='certs/')
    certificate_of_accreditation = models.FileField(upload_to='certs/')

