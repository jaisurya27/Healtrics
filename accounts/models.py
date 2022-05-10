from django.db import models
import django
import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings

class MyUserManager(BaseUserManager):
    def create_user(self, email, mobile_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not mobile_number:
            raise ValueError('Users must have a mobile number')
        user = self.model(
            email=self.normalize_email(email),
            mobile_number=self.mobile_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        user = self.create_user(
            email,
            mobile_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    mobile_number = models.TextField(max_length=255)
    user_type = models.CharField(max_length=255, choices = [('hospitals','hospitals'),('blood_banks','blood_banks'),('donor_requesters','donor_requesters'),('admin','admin')])
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    email_otp = models.CharField(max_length=6, blank=True, null=True)
    mobile_otp = models.CharField(max_length=6, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_date_time = models.DateTimeField(auto_now_add=django.utils.timezone.now)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin