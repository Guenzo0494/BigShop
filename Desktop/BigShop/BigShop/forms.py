from allauth.account.forms import SignupForm 
from django import forms
from django.contrib.auth.models import User

from products.models import Profile
  
class CustomSignupForm(SignupForm): 
    first_name = forms.CharField(max_length=30, required=False) 
    last_name = forms.CharField(max_length=30, required=False) 
    telephone = forms.CharField(max_length=15)
    
    # Override the init method
    def __init__(self, *args, **kwargs):
    #  Call the init of the parent class
        super().__init__(*args, **kwargs)
        # remove autofocus because it is in the wrong place
        # del self.fields['username'].widget.attrs['autofocus']
        
        # Hide the labels of fields
        self.fields['last_name'].label = ""
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nom'
        self.fields['last_name'].widget.attrs['class'] = 'my-form-control'
        
        self.fields['first_name'].label = ""
        self.fields['first_name'].widget.attrs['placeholder'] = 'Prenom'
        self.fields['first_name'].widget.attrs['class'] = 'my-form-control'
        
        self.fields['telephone'].label = ""
        self.fields['telephone'].widget.attrs['placeholder'] = 'Telephone'
        self.fields['telephone'].widget.attrs['class'] = 'my-form-control'
        
        self.fields['email'].label = ""
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['email'].widget.attrs['class'] = 'my-form-control'
        
        self.fields['password1'].label = ""
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password1'].widget.attrs['class'] = 'my-form-control'
        
        self.fields['password2'].label = ""
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer mot de passe'
        self.fields['password2'].widget.attrs['class'] = 'my-form-control'
    
    # Put in the custom signup logic
    def custom_signup(self, request, user):
        # set add fields from the form response
        user.first_name = self.cleaned_data['first_name'] 
        user.last_name = self.cleaned_data['last_name'] 
        telephone = self.cleaned_data['telephone']
        # Save the user's add fields to thier database record
        user.save() 
        # create profile instance
        user_profile = Profile(user=user, telephone=telephone)
        user_profile.save()
        return user 
        
    
   

   