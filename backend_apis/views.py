from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.contrib.auth.models import User  
from backend_apis.models import UserOtp,UserReferrals
import random,string 
from rest_framework.permissions import IsAuthenticated
from .models import User, UserProfile


def generateOtp():
    return "".join( random.choice(string.digits) for i in range(4)) 

class ValidateEmailView(APIView): 
  
    def post(self, request, format=None):
            
        email = request.POST.get('email')
        email_exist = User.objects.filter(email=email).exists()
        otp = generateOtp()
        if email_exist:
            user = User.objects.get(email=email)
        else:
            user = User.objects.create(email=email,username=email)
        a,b = UserOtp.objects.update_or_create(user=user)
        a.otp = otp
        a.save()
        return Response({"otp": otp,"email": email}, status=status.HTTP_200_OK)
    
class ValidateEmailAndOTPView(APIView):
   

    def post(self, request, format=None):
        email = request.data.get('email')
        otp = request.data.get('otp')
        
        try:
            user = User.objects.get(email=email)
            user_otp = UserOtp.objects.get(user=user)
            
            if user_otp.otp == otp:
             return Response({"message": "Email and OTP are valid", "userid": user.id}, status=status.HTTP_200_OK)
            
            else:
                return Response({"message": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
            
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        except UserOtp.DoesNotExist:
            return Response({"message": "User OTP entry not found"}, status=status.HTTP_400_BAD_REQUEST)
        

def generatereferralcode():
    return"".join( random.choice(string.ascii_letters) for i in range(6))

class GetInputDataAndUserid(APIView):
    
    def post(self, request, format=None):
        email = request.data.get('email')
        fullname = request.data.get('fullname')
        country = request.data.get('country')
        createpassword = request.data.get('createpassword')
        confirmpassword = request.data.get('confirmpassword')
        referral_code = request.data.get('referral_code')

        # Retrieve the user by email
        user = User.objects.get(email=email)

        referralcode = generatereferralcode()


        # Check if createpassword and confirmpassword match
        if createpassword != confirmpassword:
            return Response({"error": "Password and confirm password do not match."}, status=400)

        # Store data in the UserProfile model
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.full_name = fullname
        user_profile.country = country
        user_profile.referral_code = referral_code  # Store the referral code
        user_profile.save()
        # Store data in the UserReferrals model
        user_referrals, _ = UserReferrals.objects.get_or_create(user=user_profile)
        user_referrals.referralcode = referralcode
        user_referrals.save()

        # Example response
        response_data = {
            'message': 'Data saved successfully',
        }

        return Response({"fullname": fullname, "userid": user.id, "referralcode": referralcode}, status=status.HTTP_200_OK)