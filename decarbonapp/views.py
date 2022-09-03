from platform import uname

from django.shortcuts import render


# Create your views here.
from decarbonapp.models import Contacts


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def booking(request):
    return render(request, 'booking.html')


def contact(request):
    if request.method == 'GET':
         return render(request,'contact.html')
    else:
        name=request.POST.get('uname')
        mail=request.POST.get('gmail')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        Contacts.objects.create(name=name,gmail=mail,subject=subject,message=message)
        return render(request, 'contact.html')


def location(request):
    return render(request, 'location.html')


def price(request):
    return render(request, 'price.html')


def service(request):
    return render(request, 'service.html')


def single(request):
    return render(request, 'single.html')


def team(request):
    return render(request, 'team.html')


def flaticon(request):
    return render(request, 'flaticon.html')
