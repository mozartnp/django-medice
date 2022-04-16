from django.urls import path

from backend.patient import views as v

app_name = 'patient'

urlpatterns = [
    path('doctor/', v.doctor_list, name='doctor_list'),
    path('patient/', v.patient_list, name='patient_list'),
]
