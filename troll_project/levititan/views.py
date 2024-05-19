from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def liga(request):
    return HttpResponse('your mom')

def levititan(request):
    return TemplateResponse(request, 'levititan/levititan.html')