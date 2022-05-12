from django.urls import path
from . import views

urlpatterns = [
    path('admins_dashboard/',views.admins_dashboard,name='admins_dashboard')
]