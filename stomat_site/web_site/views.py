from django.shortcuts import render
from .models import Service, Category, Doctor


def about_clinic(request):
    clinic_name = "Medols"
    clinic_contacts = "8-951-353-31-39"
    clinic_address = "g. Kirov, ul. Proletarskaya, d. 14"

    #context = {
        #'clinic_name': clinic_name,
        #'clinic_contacts': clinic_contacts,
        #'clinic_address': clinic_address,
    #}
    #return render(request, 'about_clinic.html', context)
    return render(request, 'web_site/new_base.html')


def price_list(request):
    services = Service.objects.all()

    context = {
        'services': services,
    }
    return render(request, 'price_list.html', context)


def online_entry(request):
    doctors = Doctor.objects.all()

    context = {
        'doctors': doctors
    }
    return render(request, 'online_entry.html', context)
