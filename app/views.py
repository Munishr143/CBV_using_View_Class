from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

def fbv_string(request):
    return HttpResponse('fbv_string is executed sucessfully')

class cbv_string(View):
    def get(self, request):
        return HttpResponse('cbv_string is executed sucessfully')
    
def fbv_html(request):
    return render(request, 'fbv_html.html')

class cbv_html(View):
    def get(self, request):
        return render(request, 'cbv_html.html')
def fbv_form(request):
    SFO=Student_Form()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=Student_Form(request.POST)

        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data is inserted')
    return render(request, 'fbv_form.html', d)

class cbv_form(View):
    def get(self, request):
        SFO=Student_Form()
        d={'SFO':SFO}
        return render(request, 'cbv_form.html', d)
    
    def post(self, request):
        SFD=Student_Form(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data is inserted')


