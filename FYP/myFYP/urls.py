from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
#This is how we specify url patterns. URLS are basically controllers in DJANGO

from . import views

#period is a relative import, Basically importing views from the current pkg

# views can also be impoted using the following the line as there is only one
#app in our website

#from myFYP import views

app_name = 'myFYP'
urlpatterns = [

    url(r'^$',views.index, name='index'),
    url(r'^request_page/$',views.request_page, name='request_page'),
    url(r'^main_login/$',views.main_login,name='main_login'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^vas_login/$',views.vas_login,name='vas_login'),
    url(r'^login_page/$',views.login_page,name='login_page'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^AboutUs/$',views.about, name='AboutUs'),
    #url(r'^login/$',views.login, name='login'),
    url(r'^signup_form/$',views.signup_form, name='signup_form'),
    url(r'^localities/$',views.localities, name='localities'),
    url(r'^addproperty/$',views.addproperty, name='addproperty'),
    url(r'^services/$',views.services, name='services'),
    url(r'^confirmPassword/$',views.confirmPassword, name='ConfirmYourPassword'),
    url(r'^forgotpassword/$',views.forgotpassword, name='forgotpassword'),
    url(r'^Properties/$',views.myproperties, name='Properties'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
    url(r'^vas/$',views.services, name='vas'),
    url(r'^service_providers/$',views.service_providers, name='service_providers'),
    url(r'^contact_to_user/$',views.contact_to_user, name='contact_to_user'),
    url(r'^Contact_to_provider/$',views.Contact_to_provider, name='Contact_to_provider'),
    url(r'^myproperties/$',views.myproperties, name='myproperties'),
    url(r'^Signup_vas/$',views.Signup_vas, name='Signup_vas'),
    url(r'^propertydetails/$',views.propertydetails, name='propertydetails'),
   
      
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


