from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from requests.exceptions import ConnectionError
import driver
import json

def request_page(request):
    try:

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
    except ConnectionError as e:
        # This is the correct syntax
        print (e)
        return HttpResponse("No internet Connection")


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "home.html"
