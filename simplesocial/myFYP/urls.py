
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'myFYP'
urlpatterns = [
    url(r"^login/$", auth_views.LoginView.as_view(template_name="myFYP/login.html"),name='login'),
    url(r"^vas_login/$", auth_views.LoginView.as_view(template_name="myFYP/vas_login.html"),name='vas_login'),
	url(r'^contact/$',views.contact, name='contact'),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^signup/$", views.SignUp.as_view(), name="signup"),
	url(r'^addproperty/$',views.addproperty, name='addproperty'),
    url(r'^About-Us/$',views.About.as_view(), name='About-Us'),
    url(r'^services/$',views.Services.as_view(), name='Our-Services'),
    url(r'^nointernet/$',views.Nointernet.as_view(), name='nointernet'),
    url(r'^main_login/$',views.Main_login.as_view(),name='main_login'),
    url(r'^myproperties/$',views.myproperties, name='myproperties'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^properties/$',views.properties, name='properties'),
    #url(r'^(?P<id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^profile/(?P<product_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^localities/$',views.localities, name='localities'),
    url(r'^seeReviews/$',views.seeReviews, name='seeReviews'),
    url(r'^mustafaTown/$',views.mustafaTown, name='mustafaTown'),
    url(r'^iqbalTown/$',views.iqbalTown, name='iqbalTown'),
    url(r'^mustafaTown_properties/$',views.mustafaTown_properties, name='mustafaTown_properties'),
    url(r'^joharTown_properties/$',views.joharTown_properties, name='joharTown_properties'),
    url(r'^defence_properties/$',views.defence_properties, name='defence_properties'),
    url(r'^iqbalTown_rev/$',views.iqbalTown_rev, name='iqbalTown_rev'),
    url(r'^joharTown_rev/$',views.joharTown_rev, name='joharTown_rev'),
    url(r'^defence_rev/$',views.defence_rev, name='defence_rev'),
    url(r'^register/$',views.register,name='register'),
    url(r'^valueAddedServices/$',views.valueAddedServices,name='valueAddedServices'),
    url(r'^delete_property/(?P<product_id>[0-9]+)/$', views.delete, name='delete'),

]
