from dietapp.post_upload import post_upload
from django.shortcuts import render  
from django.template import loader  
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Signup 
from .models import Health_data
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
def index(request): 	 
	return render(request, 'dietapp/index.html') 

#@login_required(login_url='/login/')
def health_post(request): 
	return render(request, 'dietapp/post-ad.html')
@csrf_exempt
def health_data(request):
	if request.method == 'POST':
		user = Signup.objects.get(email=request.session.get('semail'))
		post=Health_data()
		post.author=user	
		post.group= request.POST.get('group')	
		post.age= request.POST.get('Age')
		post.gender= request.POST.get('Gender')
		post.title= request.POST.get('Title')
		post.des= request.POST.get('des')
		post.weight= request.POST.get('Weight')	
		post.postfile=request.FILES['postfile'].name
		post.save()
		post_upload(request.FILES['postfile']) 
		return redirect('/profile/') 

def alltype(request): 
	obj=Health_data.objects.all()
	return render(request, 'dietapp/alltype.html',{'obj':obj})

def single(request,postid=id): 
	obj=Health_data.objects.get(id=postid)
	obj.post_views=obj.post_views+1 #This will also count multiple views by a single user.
	obj.save()
	return render(request, 'dietapp/single.html',{'obj':obj}) 

@csrf_exempt
def category(request,username):
    rp = json.loads(request.body.decode('utf-8'))
    if request.method == 'POST':
    	print(rp)
    return JsonResponse({'status': 'Success', 'message': 'Recoard has been updated.'})

