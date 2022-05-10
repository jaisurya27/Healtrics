from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from .admin import UserCreationForm
import requests,math,random
from .models import *
from twilio.rest import Client
from sendgrid.helpers.mail import Mail

UserModel = get_user_model()

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for _ in range(6) : 
        OTP += digits[math.floor(random.random() * 10)]
    return OTP 

def mail_send(subject,message,email_from,recipient_list):
    message = Mail(from_email=str(email_from),to_emails=str(recipient_list[0]),subject=str(subject),html_content=str(message))
    sg = sendgrid.SendGridAPIClient(settings.SEND_GRID_API)
    sg.send(message)

def phone_otp_send(message,contact_number):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    client.messages.create(body=str(message),from_=str(contact_number))

def home(request):
    return render(request,'accounts/index.html')

def admin_signup(request):
    if request.method == "POST":
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        email_otp = generateOTP()
        mobile_otp = generateOTP()
        user = User(email=email, mobile_number=mobile_number, user_type='admin',email_otp=email_otp, mobile_otp=mobile_otp, is_admin=True)
        user.set_password(password)
        user.save()
        auth.login(request,user,backend=None)
        return redirect('admin_verify')
    else:
        return render(request,'accounts/admin_signup.html')

def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user,backend=None)
            return redirect('admin_view_exercise')
        else:
            return redirect('admin_login')
    else:
        return render(request,'accounts/admin_login.html')

def hospitals_signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User(email=email)
        user.set_password(password)
        user.save()
        auth.login(request,user,backend=None)
        return redirect('add_profile')
    else:
        return render(request,'accounts/hospital_signup.html')

def hospitals_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user,backend=None)
            return redirect('view_profile')
        else:
            return redirect('hospitals_login')
    else:
        return render(request,'accounts/hospitals_login.html')

def blood_bank_signup(request):
    pass

def blood_bank_login(request):
    pass

def requesters_donors_signup(request):
    pass

def requesters_donors_login(request):
    pass

def password_authentication(request):
    pass

def otp_verification(request):
    pass

def logout(request):
    auth.logout(request)
    return redirect('home')
