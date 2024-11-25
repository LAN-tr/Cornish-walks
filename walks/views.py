from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.

def test_message(request):
    return HttpResponse("Hello walker!")

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'    