from django.shortcuts import render, redirect,render_to_response
from myFYP.models import RegUser,Vasp
from . import forms
from myFYP.forms import NewUserForm,VasForm
import driver
#######################
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def request_page(request):
    arr = []
    if(request.GET.get('mybtn')):
        #print(request.GET.get('mybtn'))
        #print(request.GET.get('mytextbox'))
        arr = driver.mypythonfunction( int(request.GET.get('mytextbox')) )
        res = {'house_records':arr}

    return render(request,'myFYP/home.html',context=res)


def index(request):
    user_list = RegUser.objects.order_by('First_Name')
    add_dict = {'user_records':user_list}
    return render(request, 'myFYP/home.html',context=add_dict)

def contact(request):
    form1 = forms.FormName()

    if request.method == 'POST':
        form1 = forms.FormName(request.POST)

        if form1.is_valid():
            print("Validation is Successful!!!")
            #how to access that data is as follow
            print("Name: " +form1.cleaned_data['name'])
            print("Email: " +form1.cleaned_data['email'])
            print("Text: " +form1.cleaned_data['text'])


    return render(request, 'myFYP/contact.html',{'form1':form1})

def about(request):
    return render(request, 'myFYP/about.html')

def signup_form(request):

    registered = False

    if request.method == "POST":
        form = NewUserForm(data=request.POST)

        if form.is_valid():
            user  = form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(form.errors)
    else:
        form = NewUserForm()


    return render(request,'myFYP/signup_form.html',{'form':form})



def Signup_vas(request):
    registered = False

    if request.method == "POST":
        form = VasForm(data=request.POST)

        if form.is_valid():
            user  = form.save()
            #user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(form.errors)
    else:
        form = VasForm()

    return render(request,'myFYP/Signup_vas.html',{'form':form})

def login_page(request):
    return render(request, 'myFYP/login_page.html')

@login_required
def localities(request):
    return render(request, 'myFYP/localities.html')


def propertydetails(request):
    return render(request, 'myFYP/propertydetails.html')


def addproperty(request):
    return render(request, 'myFYP/submit-property.html')

def services(request):
    return render(request, 'myFYP/vas.html')

def service_providers(request):
    return render(request, 'myFYP/service_providers.html')

def contact_to_user(request):
    return render(request, 'myFYP/contact_to_user.html')

def Contact_to_provider(request):
    return render(request, 'myFYP/Contact_to_provider.html')

def myproperties(request):
    return render(request, 'myFYP/myproperties.html')

def Signup_vas(request):
    return render(request, 'myFYP/Signup_vas.html')

def confirmPassword(request):
    return render(request, 'myFYP/change-password.html')

def forgotpassword(request):
    return render(request, 'myFYP/forgotpassword.html')

def main_login(request):
    return render(request, 'myFYP/main_login.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login details!!!")
    else:
        return render(request,'myFYP/login_page.html',{})


def vas_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login details!!!")
    else:
        return render(request,'myFYP/vas_login.html',{})


@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


#render looks at templates directory in the same folder of myFYP
