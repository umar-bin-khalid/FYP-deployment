from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
import driver

def request_page(request):
    arr = {}
    if(request.GET.get('mybtn')):
        arr = driver.mypythonfunction( int(request.GET.get('myminbox')),int(request.GET.get('mymaxbox')),int(request.GET.get('mytextbox')) )
        res = {'house_records':arr}

    return render(request,'home.html',context=res)

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "home.html"
