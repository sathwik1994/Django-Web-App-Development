from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appuser,Video


class SignUp(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    password = forms.CharField(max_length=30, required=False, help_text='Optional.')
    

    class Meta:
        model = Appuser
        fields = ('username','email', 'password',)


class UpdatePassword(forms.ModelForm):
    username = forms.CharField(max_length=254,required=True )
    current_password = forms.CharField(max_length=30, required=True, help_text='Optional.')
    new_password = forms.CharField(max_length = 30, required = True)
    
    class Meta:
        model = Appuser
        fields = ('username', 'current_password','new_password')		


class LogIn(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False, help_text='Required')
    password = forms.CharField(max_length=30, required=False, help_text='Required')
    

    class Meta:
        model = Appuser
        fields = ('username', 'password',)


class DeleteUser(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False, help_text='Required')
     

    class Meta:
        model = Appuser
        fields = ('username',)



class InsertVideo(forms.ModelForm):
    title = forms.CharField(max_length = 100)
    description = forms.CharField(max_length=70)
    #created_ts = forms.DateTimeField()
    status = forms.CharField(max_length = 30)
    user_id = forms.ModelChoiceField(queryset=Appuser.objects.all())
    duration = forms.IntegerField()

    

    class Meta:
        model = Video
        fields = ('title','description','status','user_id','duration')
