from django.urls import path
from . import views

urlpatterns = [
    path('blood_banks_add_profile/',views.blood_banks_add_profile,name='blood_banks_add_profile'),
    path('blood_banks_edit_profile/',views.blood_banks_edit_profile,name='blood_banks_edit_profile'),
    path('blood_banks_view_profile/',views.blood_banks_view_profile,name='blood_banks_view_profile'),
    path('blood_banks_view_profile_link/<pid>',views.blood_banks_view_profile_link,name='blood_banks_view_profile_link'),
    path('blood_banks_add_camp/',views.blood_banks_add_camp,name='blood_banks_add_camp'),
    path('blood_banks_edit_camp/<cid>',views.blood_banks_edit_camp,name='blood_banks_edit_camp'),
    path('blood_banks_view_camps/',views.blood_banks_view_camps,name='blood_banks_view_camps'),
    path('blood_banks_view_camp/<cid>',views.blood_banks_view_camp,name='blood_banks_view_camp'),
    path('blood_banks_view_camp_analysis/<cid>',views.blood_banks_view_camp_analysis,name='blood_banks_view_camp_analysis'),
    path('blood_banks_view_blood_requests/',views.blood_banks_view_blood_requests,name='blood_banks_view_blood_requests'),
    path('blood_banks_accept_blood_request/<rid>',views.blood_banks_accept_blood_request,name='blood_banks_accept_blood_request'),
    path('blood_banks_track_blood_requests/',views.blood_banks_track_blood_requests,name='blood_banks_track_blood_requests')
]