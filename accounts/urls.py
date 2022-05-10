from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin_signup/',views.admin_signup,name='admin_signup'),
    path('admin_verify/',views.admin_verify,name='admin_verify'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('hospitals_signup/',views.hospital_signup,name='hospitals_signup'),
    path('hospitals_verify/',views.hospital_verify,name='hospitals_verify'),
    path('hospitals_login/',views.hospital_login,name='hospitals_login'),
    path('bloodbanks_signup/',views.bloodbanks_signup,name='bloodbanks_signup'),
    path('bloodbanks_verify/',views.bloodbanks_verify,name='bloodbanks_verify'),
    path('bloodbanks_login/',views.bloodbanks_login,name='bloodbanks_login'),
    path('donors_requesters_signup/',views.donors_requesters_signup,name='donors_requesters_signup'),
    path('donors_requesters_verify/',views.donors_requesters_verify,name='donors_requesters_verify'),
    path('donors_requesters_login/',views.donors_requesters_login,name='donors_requesters_login'),
    path('logout/',views.logout,name='logout')
]