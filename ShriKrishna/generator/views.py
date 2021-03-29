from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    leng = request.GET.get('length')
    
    if request.GET.get('Uppercase'):
        case = "Enabled"
    else:
        case = "Disabled"
    if request.GET.get('special'):
        spec = "Enabled"
    else:
        spec = "Disabled"

    

    all_value = "Length is " +leng+ "Upper Case is " +case+ "Special char is " + spec

    return render(request,'generator/password.html',{'password' : all_value})