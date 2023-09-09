from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponse,Http404, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

def index(request):
    respons_data = render_to_string("quotes/index.html")
    return HttpResponse(respons_data)