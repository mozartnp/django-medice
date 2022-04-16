from django.shortcuts import render


def doctor_list(request):
    template_name = 'patient/doctor_list.html'
    return render(request, template_name)


def patient_list(request):
    template_name = 'patient/patient_list.html'
    return render(request, template_name)
