from django.shortcuts import render,redirect
from .models import Appuser,Video
from .forms import SignUp, UpdatePassword, LogIn, DeleteUser, InsertVideo
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib import auth
# Create your views here.


def home(request):
	all=Appuser.objects.all()
	return render(request,'home.html',{'action':"Display all",'all':all})

def signUp(request):
	if request.method == 'POST':
		form = SignUp(request.POST)
		#print("form:"+form)
		if form.is_valid():
			sign = form.save()
			sign.username = form.cleaned_data.get('username')
			sign.email = form.cleaned_data.get('email')
			sign.password = form.cleaned_data.get('password')
			print(sign.password)
			sign.save()
			#user = authenticate(username=name, password=password)
			#login(request, user)
			return redirect('home')
	else:
		form = SignUp()
	return render(request, 'signUp.html', {'form': form})

def updatePassword(request):
	if request.method == 'POST':
		form = UpdatePassword(request.POST)
		#print("form:"+form)
		if form.is_valid():
			#sign = form.save()
			
			form.username = form.cleaned_data.get('username')
			form.current_password = form.cleaned_data.get('current_password')
			form.new_password = form.cleaned_data.get('new_password')
			valid = Appuser.objects.filter(username = form.username, password = form.current_password).values("password")
			for v in valid:
				Appuser.objects.filter(password = v.get('password')).update(password = form.new_password)
			return redirect('home')
	else:
		form = UpdatePassword()
	return render(request, 'updatePassword.html', {'form': form})

def home3(request):
	return render(request, 'home3.html')

	
        
def logIn(request):
	if request.method == 'POST':
		form = LogIn(request.POST)
		if form.is_valid():
			form.username = form.cleaned_data.get('username')
			form.password = form.cleaned_data.get('password')
			valid = Appuser.objects.filter(username = form.username, password = form.password).values()
			if valid is not None:
				return redirect('home2')
	else:
		form = LogIn()
	return render(request, 'logIn.html', {'form':form})
			

def home2(request):
	all=Video.objects.all()
	return render(request,'home2.html',{'action':"Display all",'all':all})


def deleteUser(request):
	if request.method == 'POST':
		form = DeleteUser(request.POST)
		if form.is_valid():
			form.username = form.cleaned_data.get('username')
			Appuser.objects.filter(username = form.username).delete()
			return redirect('home')

	else:
		form = DeleteUser()
	return render(request, 'deleteUser.html', {'form':form})
			
			
def insertVideo(request):
	if request.method == 'POST':
		form = InsertVideo(request.POST)
		
		if form.is_valid():
			sign = form.save()
			sign.title = form.cleaned_data.get('title')
			sign.description = form.cleaned_data.get('description')
			sign.created_ts = form.cleaned_data.get('created_ts')
			sign.status = form.cleaned_data.get('status')
			sign.duration = form.cleaned_data.get('duration')
			sign.user_id = form.cleaned_data.get('user_id')
			sign.save()
			#user = authenticate(username=name, password=password)
			#login(request, user)
			return redirect('home2')
	else:
		form = InsertVideo()
	return render(request, 'insertVideo.html', {'form': form})
		

	

			
