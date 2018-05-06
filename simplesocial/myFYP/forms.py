from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from myFYP.models import Products, Localities, Contact
from myFYP.models import UserProfileInfo
from django.contrib.auth.models import User
from django import forms
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic','type')




class ProductForm(forms.ModelForm):
    description = forms.CharField( widget=forms.Textarea)
    Rooms = forms.CharField(label='Rooms',
                    widget=forms.TextInput(attrs={'placeholder': 'No of Rooms'}))
    BathRooms = forms.CharField(label='BathRooms',
                    widget=forms.TextInput(attrs={'placeholder': 'No of BathRooms'}))
    class Meta():
        model = Products
        fields = '__all__'


class contactForm(forms.ModelForm):
    Message = forms.CharField( label='Entre Your Message along with your email:',
                              widget=forms.Textarea(attrs={'placeholder': 'Enter here...'}))
    class Meta():
        model = Contact
        fields = '__all__'




class LocalitiesForm(forms.ModelForm):
    rate_cleanliness = forms.CharField(
        label='Rate Cleanliness',
        widget=forms.TextInput(attrs={'placeholder': 'Rate out of 10'})
    )
    rate_locality = forms.CharField(
        label='Rate locality',
        widget=forms.TextInput(attrs={'placeholder': 'Rate out of 10'})
    )
    rate_security = forms.CharField(
        label='Rate security',
        widget=forms.TextInput(attrs={'placeholder': 'Rate out of 10'})
    )
    rate_parks = forms.CharField(
        label='Rate parks',
        widget=forms.TextInput(attrs={'placeholder': 'Rate out of 10'})
    )
    playGrounds = forms.CharField(
        label='Rate playGrounds',
        widget=forms.TextInput(attrs={'placeholder': 'Rate out of 10'})
    )
    class Meta:
        model = Localities
        fields = '__all__'
