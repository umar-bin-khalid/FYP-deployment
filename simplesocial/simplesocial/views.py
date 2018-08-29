from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from requests.exceptions import ConnectionError
import driver
import aarzdriver
import json

def request_page(request):

    zcheck = str(request.GET.get('website'))
    if ( zcheck == "Zameen"):

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
                arr = driver.mypythonfunction( str(final),float(request.GET.get('myminbox')),float(request.GET.get('mymaxbox')), purpose )
                res = {'house_records':arr}

            return render(request,'home.html',context=res)
        except ConnectionError as e:
            # This is the correct syntax
            prfloat (e)
            return HttpResponseRedirect("/myFYP/nointernet/")
    else:

        try:


            arr1 = {}
            pur1 = str(request.GET.get('mytextbox'))

            if( pur1 == "Buy"):
                purpose1 = 0
            if(pur1 == "Rent"):
                purpose1 = 1

            if(request.GET.get('mybtn')):
                arr1 = aarzdriver.mypythonfunction( str(request.GET.get('locations')),float(request.GET.get('myminbox')),float(request.GET.get('mymaxbox')), purpose1 )
                res1 = {'aarzhouse_records':arr1}
                print(res1)
            return render(request,'home.html',context=res1)

        except ConnectionError as e:
            # This is the correct syntax
            print (e)
            return HttpResponseRedirect("/myFYP/nointernet/")





class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "home.html"
