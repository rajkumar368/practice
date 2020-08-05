from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('patient_signup', views.patient_signup, name="patient_signup"),
    path('doctor_signup', views.doctor_signup, name="doctor_signup"),
    path('clinic_admin_signup', views.clinic_admin_signup, name="clinic_admin_signup"),
    path('logins', views.logins, name="logins"),
]