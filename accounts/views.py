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
    client.messages.create(body=str(message),from_=settings.SMS_HOST_NUMBER,to=contact_number)

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
        mail_send("account_verification",email_otp,settings.EMAIL_HOST_USER,[email])
        phone_otp_send(mobile_otp,mobile_number)
        auth.login(request,user,backend=None)
        return redirect('admin_verify')
    else:
        return render(request,'accounts/admin_signup.html')

def admin_verify(request):
    if request.method=='POST':
        email_otp = request.POST['email_otp']
        mobile_otp = request.POST['mobile_otp']
        user = User.objects.filter(pk=request.user.pk).first()
        if user.email_otp==email_otp and user.mobile_otp==mobile_otp:
            user.is_email_verified=True
            user.is_mobile_verified=True
            user.save()
            return redirect('admin_dashboard') 
    else:
        return render(request,'accounts/admin_verify.html')

def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None and user.user_type=='admin':
            auth.login(request,user,backend=None)
            return redirect('admin_dashboard')
        else:
            return redirect('admin_login')
    else:
        return render(request,'accounts/admin_login.html')

def hospital_signup(request):
    if request.method == "POST":
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        email_otp = generateOTP()
        mobile_otp = generateOTP()
        user = User(email=email, mobile_number=mobile_number, user_type='hospitals',email_otp=email_otp, mobile_otp=mobile_otp, is_admin=True)
        user.set_password(password)
        user.save()
        mail_send("account_verification",email_otp,settings.EMAIL_HOST_USER,[email])
        phone_otp_send(mobile_otp,mobile_number)
        auth.login(request,user,backend=None)
        return redirect('hospitals_verify')
    else:
        return render(request,'accounts/hospitals_signup.html')

def hospital_verify(request):
    if request.method=='POST':
        email_otp = request.POST['email_otp']
        mobile_otp = request.POST['mobile_otp']
        user = User.objects.filter(pk=request.user.pk).first()
        if user.email_otp==email_otp and user.mobile_otp==mobile_otp:
            user.is_email_verified=True
            user.is_mobile_verified=True
            user.save()
            return redirect('view_hospital_profile') 
    else:
        return render(request,'accounts/hospitals_verify.html')

def hospital_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None and user.user_type=='hospitals':
            auth.login(request,user,backend=None)
            return redirect('view_hospital_profile')
        else:
            return redirect('hospitals_login')
    else:
        return render(request,'accounts/hospitals_login.html')

def bloodbanks_signup(request):
    if request.method == "POST":
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        email_otp = generateOTP()
        mobile_otp = generateOTP()
        user = User(email=email, mobile_number=mobile_number, user_type='blood_banks',email_otp=email_otp, mobile_otp=mobile_otp, is_admin=True)
        user.set_password(password)
        user.save()
        mail_send("account_verification",email_otp,settings.EMAIL_HOST_USER,[email])
        phone_otp_send(mobile_otp,mobile_number)
        auth.login(request,user,backend=None)
        return redirect('bloodbanks_verify')
    else:
        return render(request,'accounts/bloodbanks_signup.html')

def bloodbanks_verify(request):
    if request.method=='POST':
        email_otp = request.POST['email_otp']
        mobile_otp = request.POST['mobile_otp']
        user = User.objects.filter(pk=request.user.pk).first()
        if user.email_otp==email_otp and user.mobile_otp==mobile_otp:
            user.is_email_verified=True
            user.is_mobile_verified=True
            user.save()
            return redirect('view_bloodbank_profile') 
    else:
        return render(request,'accounts/bloodbank_verify.html')

def bloodbanks_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None and user.user_type=='blood_banks':
            auth.login(request,user,backend=None)
            return redirect('bloodbanks_dashboard')
        else:
            return redirect('bloodbanks_login')
    else:
        return render(request,'accounts/bloodbanks_login.html')

def donors_requesters_signup(request):
    if request.method == "POST":
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        email_otp = generateOTP()
        mobile_otp = generateOTP()
        user = User(email=email, mobile_number=mobile_number, user_type='donors_requesters',email_otp=email_otp, mobile_otp=mobile_otp, is_admin=True)
        user.set_password(password)
        user.save()
        mail_send("account_verification",email_otp,settings.EMAIL_HOST_USER,[email])
        phone_otp_send(mobile_otp,mobile_number)
        auth.login(request,user,backend=None)
        return redirect('view_donors_requesters_profile')
    else:
        return render(request,'accounts/donors_requesters_signup.html')

def donors_requesters_verify(request):
    if request.method=='POST':
        email_otp = request.POST['email_otp']
        mobile_otp = request.POST['mobile_otp']
        user = User.objects.filter(pk=request.user.pk).first()
        if user.email_otp==email_otp and user.mobile_otp==mobile_otp:
            user.is_email_verified=True
            user.is_mobile_verified=True
            user.save()
            return redirect('view_donors_requesters_profile') 
    else:
        return render(request,'accounts/donors_requesters_verify.html')

def donors_requesters_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None and user.user_type=='donors_requesters':
            auth.login(request,user,backend=None)
            return redirect('view_donors_requesters_profile')
        else:
            return redirect('donors_requesters_login')
    else:
        return render(request,'accounts/donors_requesters_login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
