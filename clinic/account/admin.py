from django.contrib import admin
from account.models import Patient,Doctor,Clinic_admin

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Clinic_admin)
