from django.shortcuts import render
from .models import *
# Create your views here.

@login_required(login_url='donors_requesters_login')
def add_profile(request):
    if request.method=="POST":
        full_name = request.POST['full_name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        blood_group = request.POST['blood_group']
        address = request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        country = request.POST['country']
        zipcode = request.POST['zipcode']
        aadhar_number = request.POST['aadhar_number'] # have to encrypt
        contact_email = request.POST['contact_email']
        contact_number = request.POST['contact_number']
        profile_pic = request.FILES['profile_pic']
        last_donation_date = request.POST['last_donation_date']
        profile = Profile(user=request.user,full_name=full_name,gender=gender,dob=dob, blood_group=blood_group, address=address, state=state, city=city, country=country, zipcode=zipcode, aadhar_number=aadhar_number, contact_email=contact_email, contact_number=contact_number, profile_pic=profile_pic,last_donation_date=last_donation_date)
        profile.save()
        return redirect('view_profile')
    else:
        return render(request,'user_app/add_profile.html')

@login_required(login_url='donors_requesters_login')
def edit_profile(request):
    if request.method=="POST":
        profile = Profile.objects.filter(user=request.user).first()
        profile.full_name = request.POST['full_name']
        profile.gender = request.POST['gender']
        profile.dob = request.POST['dob']
        profile.blood_group = request.POST['blood_group']
        profile.address = request.POST['address']
        profile.state = request.POST['state']
        profile.city = request.POST['city']
        profile.country = request.POST['country']
        profile.zipcode = request.POST['zipcode']
        profile.aadhar_number = request.POST['aadhar_number'] # have to encrypt
        profile.contact_email = request.POST['contact_email']
        profile.contact_number = request.POST['contact_number']
        profile.profile_pic = request.FILES['profile_pic']
        profile.last_donation_date = request.POST['last_donation_date']
        profile.save()
        return redirect('view_donor')
    else:
        return render(request,'donors_requesters/edit_profile.html')

def view_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    return render(request, 'donors_requesters/view_profile.html', {'profile':profile})

def search_camps(request):
    pass

def view_camp_participated(request, uid):
    camps = ParticipateCamp.objects.filter(profile=request.profile).all()
    return render(request,'donors_requesters/viewcamp-participated.html',{'camps':camps})

def view_camp_ongoing(request):
    camps = ParticipateCamp.objects.filter(blood_camp=request.bloodcamp).all().order_by('-expiry_date')
    return render(request, 'donors_requesters/view_camp-ongoing.html',{'camps':camps})

def add_request_for_blood(request):
    if request.method=='POST':
        request_date_time = request.POST['request_date_time']
        request_duration = request.POST['request_duration']
        blood_type_needed = request.POST['blood_type_needed']
        address = request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        country = request.POST['country']
        zipcode = request.POST['zipcode']
        contact_email = request.POST['contact_email']
        contact_number = request.POST['contact_number']
        blood_request = BloodRequest(requester_profile=request.profile, hospital_profile = request.hospital, request_date_time=request_date_time, request_duration=request_duration, blood_type_needed=blood_type_needed, address=address, state=state, city=city, country=country, zipcode=zipode, contact_email=contact_email, contact_number=contact_number)
        blood_request.save()
        return redirect('')
def view_request_for_blood(request):
    pass

def view_accept_blood_donation_request(request):
    pass

