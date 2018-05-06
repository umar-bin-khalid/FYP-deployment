from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
import driver
import json

def request_page(request):
    loc = str(request.GET.get('locations'))

    with open('zameenlocations.json') as f:
        data = json.load(f)
        final = data[loc]["link"]

    arr = {}
    pur = str(request.GET.get('mytextbox'))

    if( pur == "Buy"):
        purpose = 0
    if(pur == "Rent"):
        purpose = 1

    if(request.GET.get('mybtn')):
        arr = driver.mypythonfunction( str(final),int(request.GET.get('myminbox')),int(request.GET.get('mymaxbox')), purpose )
        res = {'house_records':arr}

    return render(request,'home.html',context=res)

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "home.html"
