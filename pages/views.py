from pydoc import doc
from django.shortcuts import render
from .models import Doctor

# Create your views here.
def home(request):
    doctors = Doctor.objects.all()

    data = {
        'doctors': doctors,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')