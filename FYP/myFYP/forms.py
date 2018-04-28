from django import forms
from django.core import validators
from myFYP.models import RegUser,Vasp
from django.contrib.auth.models import User
#check for the django validators documentation. There is a lot of information
#there

##def check_for_name(value):
##    test_pattern = [r'\w+']
##    if value[0] != test_pattern:
##        raise forms.ValidationError("Name is incorrect!!!")
#validators=[check_for_name]
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label="Enter your email")
    verify_email =  forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    fraudcatcher = forms.CharField(required=False,
                                   widget=forms.HiddenInput,
                                   validators=[validators.MaxLengthValidator(0)])


        
class VasForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = Vasp
        fields = '__all__'


        
class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username','email','password')
    

#clean the entire form at once
##    def clean(self):
##        all_clean_data = super().clean()
##        email = all_clean_data['email']
##        vemail = all_clean_data['verify_email']
##
##        if email != vemail:
##            raise forms.ValidationError("EMAIL DOES NOT MATCH")

    

