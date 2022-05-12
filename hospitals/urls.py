from django.urls import path
from . import views

urlpatterns = [
    path('hospitals_add_profile/',views.hospitals_add_profile,name='hospitals_add_profile'),
    path('hospitals_edit_profile/',views.hospitals_edit_profile,name='hospitals_edit_profile'),
    path('hospitals_view_profile/',views.hospitals_view_profile,name='hospitals_view_profile'),
    path('hospitals_authenticate_blood_requests/<rid>',views.hospitals_authenticate_blood_requests,name='hospitals_authenticate_blood_requests'),
    path('hospitals_track_blood_requests/',views.hospitals_track_blood_requests,name='hospitals_track_blood_requests'),
]