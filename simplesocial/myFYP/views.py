from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,TemplateView
from myFYP.models import Products,Localities,Contact,UserProfileInfo, User
from myFYP.forms import ProductForm,LocalitiesForm,contactForm, UserForm, UserProfileInfoForm
from . import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError, EmailMessage

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "myFYP/signup.html"


@login_required(login_url='/myFYP/signup/')
def delete(request, product_id):
    product = Products.objects.get(id=product_id)
    product.delete()
    #message.success(request,"deleted")
    return properties(request)



def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST,)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            Phone_Number = form.cleaned_data['Phone_Number']
            message = form.cleaned_data['Message']
            name = form.cleaned_data['name']
            #form = [str(message)]
            #form = [message,'Phone_Number',Phone_Number, 'name',name]
            email = EmailMessage(subject,message,
                                     from_email,
                                     ['smackburg@gmail.com', 'umar.ubk@gmail.com'],
                                     reply_to=[from_email])
            email.send()

            form = contactForm()
            return render(request, 'myFYP/contact.html', {
                'form': form
            })
            '''
            if subject and message and from_email:
                try:
                    send_mail(subject,
                              str(form),
                              from_email,
                              ['smackburg@gmail.com'],
                              fail_silently=False)
                    return contact(request)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                    '''
                #messages.success(request, 'Enquiry email successfully sent')
                #return render(request, 'myFYP/contact.html', {
                #    'form': form
                #})
            '''
            form.save()
            return contact(request)
            '''
    else:
        form = contactForm()
        return render(request, 'myFYP/contact.html', {
            'form': form
        })

class Addproperty(TemplateView):
    template_name = "myFYP/submit-property.html"


class About(TemplateView):
    template_name = "myFYP/about.html"

class Services(TemplateView):

    template_name = "myFYP/vas.html"

class Main_login(TemplateView):
    template_name = "myFYP/main_login.html"

@login_required(login_url='/myFYP/signup/')
def valueAddedServices(request):
    #users = User.objects.all()
    vas = UserProfileInfo.objects.select_related("user").all()
    return render(request, 'myFYP/services.html',{'vas':vas
                                                  })
@login_required(login_url='/myFYP/signup/')
def addproperty(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return myproperties(request)
    else:
        form = ProductForm()
    return render(request, 'myFYP/submit-property.html', {
        'form': form
    })

def myproperties(request):
    products = Products.objects.all()
    return render(request, 'myFYP/myproperties.html',{'products':products})
def iqbalTown(request):
    products = Products.objects.filter(location="iqbal town")
    return render(request, 'myFYP/myproperties.html',{'products':products})

def mustafaTown_properties(request):
    products = Products.objects.filter(location="mustafa town")
    return render(request, 'myFYP/myproperties.html',{'products':products})
def joharTown_properties(request):
    products = Products.objects.filter(location="johar town")
    return render(request, 'myFYP/myproperties.html',{'products':products})
def defence_properties(request):
    products = Products.objects.filter(location="defence")
    return render(request, 'myFYP/myproperties.html',{'products':products})


def detail(request ,product_id):
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        raise Http404('This products does not exist')
    return render(request, 'myFYP/propertydetail.html',{'product':product})

def properties(request):
    products = Products.objects.filter(user=request.user)
    return render(request, 'myFYP/userProperties.html',{'products':products})

@login_required(login_url='/myFYP/signup/')
def edit(request,product_id=None):
    instance = get_object_or_404(Products , id = product_id)
    form = ProductForm(request.POST or None,request.FILES,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return detail(request ,product_id)
    context = {
        "instance" : instance,
        "form" : form,
    }
    return render(request, "myFyp/submit-property.html", context)

"""
    try:
            #product = Products.objects.get(id=product_id)
        instance = Products.objects.get(id=prop_id)
        form = ProductForm(request.POST or None, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return properties(request)
        context = {
            "instance":instance,
            "form":form
        }
        return render(request, 'myFYP/update_form.html', context)
    except Products.DoesNotExist:
            raise Http404('This products does not exist')
"""
#def edit(request):
#    return render(request, 'myFYP/contact.html')

@login_required(login_url='/myFYP/signup/')
def localities(request):
    form = LocalitiesForm()

    if request.method == "POST":
        form = LocalitiesForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return seeReviews(request)
        else:
            return contact(request)
    return render(request, 'myFYP/addLocality.html',{'form': form})

def seeReviews(request):
    return render(request, 'myFYP/localities.html')

def mustafaTown(request):
    reviews = Localities.objects.filter(location="mustafa town")
    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews})
def iqbalTown_rev(request):
    reviews = Localities.objects.filter(location="iqbal town")
    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews})

def joharTown_rev(request):
    reviews = Localities.objects.filter(location="johar town")
    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews})


def defence_rev(request):
    reviews = Localities.objects.filter(location="defence")
    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews})


def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()


            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'myFYP/Signup_vas.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
