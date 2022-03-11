from pydoc import doc
from django.shortcuts import render
from .models import Doctor, Founder


# Create your views here.
def home(request):
    doctors = Doctor.objects.all()

    data = {
        'doctors': doctors,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    founders = Founder.objects.all()

    data = {
        'founders': founders,
    }
    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

# def findadoctor(request):
#     return render(request, 'pages/findadoctor.html')