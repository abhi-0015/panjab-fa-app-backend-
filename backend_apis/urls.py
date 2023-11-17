from django.urls import path
from .views import ValidateEmailView,ValidateEmailAndOTPView,GetInputDataAndUserid
from backend_apis import views

urlpatterns = [
    path('validate_email/', ValidateEmailView.as_view(), name='validate_email'),
    path('validate_otp/', ValidateEmailAndOTPView.as_view(), name='validate_otp'),
    path('getinputdata/', GetInputDataAndUserid.as_view(), name='getinputdata'),
]

 
