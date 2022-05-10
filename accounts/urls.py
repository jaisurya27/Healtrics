from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin_signup/',views.admin_signup,name='admin_signup'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('hospital_signup/',views.user_signup,name='hospital_signup'),
    path('hospital_login/',views.user_login,name='hospital_login'),
    path('blood_banks_signup/',views.user_signup,name='blood_banks_signup'),
    path('blood_banks_login/',views.user_login,name='blood_banks_login'),
    path('donors_requesters_signup/',views.user_signup,name='donors_requesters_signup'),
    path('donors_requesters_login/',views.user_login,name='donors_requesters_login'),
    path('logout/',views.logout,name='logout')
]