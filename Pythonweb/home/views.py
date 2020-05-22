from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from . import forms (khong the de import cho nay vi se gay deadlock)

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error(request,exception):
    return render(request, 'pages/error.html', {'message': exception})

def register(request):
    from .forms import RegistrationForm
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})