from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from myFYP.models import Products, Localities, Contact
from myFYP.models import UserProfileInfo
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator

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
        fields = ('profile_pic','type')


class ProductForm(forms.ModelForm):
    description = forms.CharField( widget=forms.Textarea)
    Rooms = forms.IntegerField(label='Rooms',
                    widget=forms.TextInput(attrs={'placeholder': 'No of Rooms'}))
    BathRooms = forms.IntegerField(label='BathRooms',
                    widget=forms.TextInput(attrs={'placeholder': 'No of BathRooms'}))

    class Meta():
        model = Products
        fields = '__all__'


class contactForm(forms.ModelForm):
    Message = forms.CharField( label='Entre Your Message along with your email:',
                              widget=forms.Textarea(attrs={'placeholder': 'Enter here...'}))
    email = forms.EmailField()
    class Meta():
        model = Contact
        fields = '__all__'




class LocalitiesForm(forms.ModelForm):
    rate_cleanliness = forms.IntegerField(min_value=0, max_value=5,
        label='Rate Cleanliness',
        widget=forms.NumberInput(attrs={'placeholder': 'Rate out of 5'})
    )
    rate_locality = forms.IntegerField(min_value=0, max_value=5,
        label='Rate locality',
        widget=forms.NumberInput(attrs={'placeholder': 'Rate out of 5'})
    )
    rate_security = forms.IntegerField(min_value=0, max_value=5,
        label='Rate security',
        widget=forms.NumberInput(attrs={'placeholder': 'Rate out of 5'})
    )
    rate_parks = forms.IntegerField(min_value=0, max_value=5,
        label='Rate parks',
        widget=forms.NumberInput(attrs={'placeholder': 'Rate out of 5'})
    )
    playGrounds = forms.IntegerField(min_value=0, max_value=5,
        label='Rate playGrounds',
        widget=forms.NumberInput(attrs={'placeholder': 'Rate out of 5'})
    )
    class Meta:
        model = Localities
        fields = '__all__'
