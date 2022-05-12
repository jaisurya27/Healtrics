from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admins_signup/',views.admins_signup,name='admins_signup'),
    path('admins_verify/',views.admins_verify,name='admins_verify'),
    path('admins_login/',views.admins_login,name='admins_login'),
    path('hospitals_signup/',views.hospitals_signup,name='hospitals_signup'),
    path('hospitals_verify/',views.hospitals_verify,name='hospitals_verify'),
    path('hospitals_login/',views.hospitals_login,name='hospitals_login'),
    path('blood_banks_signup/',views.blood_banks_signup,name='blood_banks_signup'),
    path('blood_banks_verify/',views.blood_banks_verify,name='blood_banks_verify'),
    path('blood_banks_login/',views.blood_banks_login,name='blood_banks_login'),
    path('donors_requesters_signup/',views.donors_requesters_signup,name='donors_requesters_signup'),
    path('donors_requesters_verify/',views.donors_requesters_verify,name='donors_requesters_verify'),
    path('donors_requesters_login/',views.donors_requesters_login,name='donors_requesters_login'),
    path('logout/',views.logout,name='logout')
]