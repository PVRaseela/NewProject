from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('retrieved')

def hellowor(request):
    return render(request,'index.html')