from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from myFYP.models import Products,Localities,Contact,UserProfileInfo, User
from myFYP.forms import ProductForm,LocalitiesForm,contactForm, UserForm, UserProfileInfoForm
from django.shortcuts import get_object_or_404, redirect, reverse
from . import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.contrib.messages import constants as messages
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404, HttpResponseNotFound, HttpResponse
from django.db.models import Avg, IntegerField

class Nointernet(TemplateView):
    template_name = "myFYP/nointernet.html"

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
                                     ['estatemerkez@gmail.com'],
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

# class Main_login(TemplateView):
#     template_name = "myFYP/main_login.html"

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
            current_user = request.user
            emailad = current_user.email
            email = EmailMessage('Property Added ', 'You have just uploaded a property on our site EstateMerkez.com.The charges for per property upload is 500. if you pay this amount then your property will be displayed otherwise this will be removed by the adminself.for payment Contact : 03364738660 ',
                                 'estatemerkez@gmail.com',
                                 [emailad],
                                 reply_to=['estatemerkez@gmail.com'])
            email.send()
            form.save()
            return myproperties(request)
    else:
        form = ProductForm()
    return render(request, 'myFYP/submit-property.html', {
        'form': form
    })


def myproperties(request):
    try:
        products = Products.objects.all()
    except products.DoesNotExist:
        raise Http404("Property Does Not Exist")
    return render(request, 'myFYP/myproperties.html',{'products':products})

def iqbalTown(request):
    try:
        products = Products.objects.filter(location="iqbal town")
    except products.DoesNotExist:
        raise Http404("Property Does Not Exist")
    return render(request, 'myFYP/myproperties.html',{'products':products})

def mustafaTown_properties(request):
    try:
        products = Products.objects.filter(location="mustafa town")
    except products.DoesNotExist:
        raise Http404("Property Does Not Exist")
    return render(request, 'myFYP/myproperties.html',{'products':products})


def joharTown_properties(request):
    try:
        products = Products.objects.filter(location="johar town")
    except products.DoesNotExist:
        raise Http404("Property Does Not Exist")
    return render(request, 'myFYP/myproperties.html',{'products':products})


def defence_properties(request):
    try:
        products = Products.objects.filter(location="defence")
    except products.DoesNotExist:
        raise Http404("Property Does Not Exist")
    return render(request, 'myFYP/myproperties.html',{'products':products})


def detail(request ,product_id):
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        return render(request, 'myFYP/404.html')
    return render(request, 'myFYP/propertydetail.html',{'product':product})

def properties(request):
    try:
        products = Products.objects.filter(user=request.user)
    except Products.DoesNotExist:
        raise Http404('This products does not exist')
    return render(request, 'myFYP/userProperties.html',{'products':products})

@login_required(login_url='/myFYP/signup/')
def edit(request,pk):
    template = 'myFYP/submit-property.html'
    products = get_object_or_404(Products, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=products)

        try:
            if form.is_valid():
                form.save()
                return properties(request)
        except Exception as e:
            messages.warning(request,'your post not saved as an error : {}'.format(e));
    else:
        form = ProductForm(instance=products)

    context = {
        'form' : form,
        'products' : products,
    }
    return render(request, template, context)

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
    reviews1 = Localities.objects.filter(location="mustafa town")
    average1 = reviews1.aggregate(average1=Avg('rate_locality' , output_field=IntegerField()))

    reviews2 = Localities.objects.filter(location="johar town")
    average2 = reviews2.aggregate(average2=Avg('rate_locality', output_field=IntegerField()))

    reviews3 = Localities.objects.filter(location="iqbal town")
    average3 = reviews3.aggregate(average3=Avg('rate_locality', output_field=IntegerField()))

    reviews4 = Localities.objects.filter(location="defence")
    average4 = reviews4.aggregate(average4=Avg('rate_locality', output_field=IntegerField()))

    reviews5 = Localities.objects.filter(location="Awan town")
    average5 = reviews5.aggregate(average5=Avg('rate_locality', output_field=IntegerField()))

    reviews6 = Localities.objects.filter(location="Wapda town")
    average6 = reviews6.aggregate(average6=Avg('rate_locality', output_field=IntegerField()))

    reviews7 = Localities.objects.filter(location="Eden")
    average7 = reviews7.aggregate(average7=Avg('rate_locality', output_field=IntegerField()))

    reviews8 = Localities.objects.filter(location="Lake city")
    average8 = reviews8.aggregate(average8=Avg('rate_locality', output_field=IntegerField()))


    return render(request, 'myFYP/localities.html',{'average1' : average1 , 'average2' : average2 ,
                                                    'average3' : average3 , 'average4' : average4 ,
                                                    'average5' : average5 , 'average6' : average6 ,
                                                    'average7' : average7 , 'average8' : average8 ,
                                                    })

def mustafaTown(request):
    reviews = Localities.objects.filter(location="mustafa town")

    average = reviews.aggregate(average=Avg('rate_locality', output_field=IntegerField()))
    parks = reviews.aggregate(parks=Avg('rate_parks', output_field=IntegerField()))
    security = reviews.aggregate(security=Avg('rate_security', output_field=IntegerField()))
    cleanliness = reviews.aggregate(cleanliness=Avg('rate_cleanliness', output_field=IntegerField()))
    playgrounds = reviews.aggregate(playgrounds=Avg('playGrounds', output_field=IntegerField()))

    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews , 'average' : average ,
                                                        'parks' : parks, 'security' : security,
                                                        'cleanliness' : cleanliness,
                                                        'playgrounds' : playgrounds
                                                        })

def iqbalTown_rev(request):
    reviews = Localities.objects.filter(location="iqbal town")

    average = reviews.aggregate(average=Avg('rate_locality', output_field=IntegerField()))
    parks = reviews.aggregate(parks=Avg('rate_parks', output_field=IntegerField()))
    security = reviews.aggregate(security=Avg('rate_security', output_field=IntegerField()))
    cleanliness = reviews.aggregate(cleanliness=Avg('rate_cleanliness', output_field=IntegerField()))
    playgrounds = reviews.aggregate(playgrounds=Avg('playGrounds', output_field=IntegerField()))

    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews , 'average' : average ,
                                                        'parks' : parks, 'security' : security,
                                                        'cleanliness' : cleanliness,
                                                        'playgrounds' : playgrounds
                                                        })

def joharTown_rev(request):
    reviews = Localities.objects.filter(location="johar town")

    average = reviews.aggregate(average=Avg('rate_locality', output_field=IntegerField()))
    parks = reviews.aggregate(parks=Avg('rate_parks', output_field=IntegerField()))
    security = reviews.aggregate(security=Avg('rate_security', output_field=IntegerField()))
    cleanliness = reviews.aggregate(cleanliness=Avg('rate_cleanliness', output_field=IntegerField()))
    playgrounds = reviews.aggregate(playgrounds=Avg('playGrounds', output_field=IntegerField()))

    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews , 'average' : average ,
                                                        'parks' : parks, 'security' : security,
                                                        'cleanliness' : cleanliness,
                                                        'playgrounds' : playgrounds
                                                        })


def defence_rev(request):
    reviews = Localities.objects.filter(location="defence")

    average = reviews.aggregate(average=Avg('rate_locality', output_field=IntegerField()))
    parks = reviews.aggregate(parks=Avg('rate_parks', output_field=IntegerField()))
    security = reviews.aggregate(security=Avg('rate_security', output_field=IntegerField()))
    cleanliness = reviews.aggregate(cleanliness=Avg('rate_cleanliness', output_field=IntegerField()))
    playgrounds = reviews.aggregate(playgrounds=Avg('playGrounds', output_field=IntegerField()))

    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews , 'average' : average ,
                                                        'parks' : parks, 'security' : security,
                                                        'cleanliness' : cleanliness,
                                                        'playgrounds' : playgrounds
                                                        })

def awan_rev(request):
    reviews = Localities.objects.filter(location="Awan town")

    average = reviews.aggregate(average=Avg('rate_locality', output_field=IntegerField()))
    parks = reviews.aggregate(parks=Avg('rate_parks', output_field=IntegerField()))
    security = reviews.aggregate(security=Avg('rate_security', output_field=IntegerField()))
    cleanliness = reviews.aggregate(cleanliness=Avg('rate_cleanliness', output_field=IntegerField()))
    playgrounds = reviews.aggregate(playgrounds=Avg('playGrounds', output_field=IntegerField()))

    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews , 'average' : average ,
                                                        'parks' : parks, 'security' : security,
                                                        'cleanliness' : cleanliness,
                                                        'playgrounds' : playgrounds
                                                        })

def wapda_Rev(request):
    reviews = Localities.objects.filter(location="Wapda town")

    average = reviews.aggregate(average=Avg('rate_locality', output_field=IntegerField()))
    parks = reviews.aggregate(parks=Avg('rate_parks', output_field=IntegerField()))
    security = reviews.aggregate(security=Avg('rate_security', output_field=IntegerField()))
    cleanliness = reviews.aggregate(cleanliness=Avg('rate_cleanliness', output_field=IntegerField()))
    playgrounds = reviews.aggregate(playgrounds=Avg('playGrounds', output_field=IntegerField()))

    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews , 'average' : average ,
                                                        'parks' : parks, 'security' : security,
                                                        'cleanliness' : cleanliness,
                                                        'playgrounds' : playgrounds
                                                        })

def eden_rev(request):
    reviews = Localities.objects.filter(location="Eden")

    average = reviews.aggregate(average=Avg('rate_locality', output_field=IntegerField()))
    parks = reviews.aggregate(parks=Avg('rate_parks', output_field=IntegerField()))
    security = reviews.aggregate(security=Avg('rate_security', output_field=IntegerField()))
    cleanliness = reviews.aggregate(cleanliness=Avg('rate_cleanliness', output_field=IntegerField()))
    playgrounds = reviews.aggregate(playgrounds=Avg('playGrounds', output_field=IntegerField()))

    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews , 'average' : average ,
                                                        'parks' : parks, 'security' : security,
                                                        'cleanliness' : cleanliness,
                                                        'playgrounds' : playgrounds
                                                        })

def lake_rev(request):
    reviews = Localities.objects.filter(location="Lake city")

    average = reviews.aggregate(average=Avg('rate_locality', output_field=IntegerField()))
    parks = reviews.aggregate(parks=Avg('rate_parks', output_field=IntegerField()))
    security = reviews.aggregate(security=Avg('rate_security', output_field=IntegerField()))
    cleanliness = reviews.aggregate(cleanliness=Avg('rate_cleanliness', output_field=IntegerField()))
    playgrounds = reviews.aggregate(playgrounds=Avg('playGrounds', output_field=IntegerField()))

    return render(request, 'myFYP/detailedReview.html',{'reviews': reviews , 'average' : average ,
                                                        'parks' : parks, 'security' : security,
                                                        'cleanliness' : cleanliness,
                                                        'playgrounds' : playgrounds
                                                        })


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
