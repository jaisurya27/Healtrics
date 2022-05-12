from django.urls import path
from . import views

urlpatterns = [
    path('donors_requesters_add_profile/',views.donors_requesters_add_profile,name='donors_requesters_add_profile'),
    path('donors_requesters_edit_profile/',views.donors_requesters_edit_profile,name='donors_requesters_edit_profile'),
    path('donors_requesters_view_profile/',views.donors_requesters_view_profile,name='donors_requesters_view_profile'),
    path('donors_requesters_search_camps/',views.donors_requesters_search_camps,name='donors_requesters_search_camps'),
    path('donors_requesters_view_camps_participated/',views.donors_requesters_view_camps_participated,name='donors_requesters_view_camps_participated'),
    path('donors_requesters_view_camps_upcoming/',views.donors_requesters_view_camps_upcoming,name='donors_requesters_view_camps_upcoming'),
    path('donors_requesters_add_donor_request/',views.donors_requesters_add_donor_request,name='donors_requesters_add_donor_request'),
    path('donors_requesters_view_donor_requests/',views.donors_requesters_view_donor_requests,name='donors_requesters_view_donor_requests'),
    path('donors_requesters_track_donor_requests/',views.donors_requesters_track_donor_requests,name='donors_requesters_track_donor_requests'),
    path('donors_requesters_view_blood_requests/',views.donors_requesters_view_blood_requests,name='donors_requesters_view_blood_requests'),
    path('donors_requesters_accept_blood_request/<rid>',views.donors_requesters_accept_blood_request,name='donors_requesters_accept_blood_request'),
    path('donors_requesters_track_blood_requests/',views.donors_requesters_track_blood_requests,name='donors_requesters_track_blood_requests'),
]