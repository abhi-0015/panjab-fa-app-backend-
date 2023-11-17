from typing import Self
from django.db import models
from django.contrib.auth.models import User
import string
import random 

class UserOtp(models.Model):
    otp = models.CharField(max_length=10)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with the User model
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    referral_code = models.CharField(max_length=20, blank=True, null=True)

class UserReferrals(models.Model):
    referralcode = models.CharField(max_length=10)
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

   

