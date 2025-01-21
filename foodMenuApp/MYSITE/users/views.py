from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages



from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

from django.contrib.auth import logout
# Create your views here.
def register(request):
    context={}
    if request.method == "POST":
       form = RegisterForm(request.POST)
       if form.is_valid():
          username = form.cleaned_data.get('username')
          messages.success(request,f'Welcome {username} Heheeheh')
          form.save()    
          return redirect('/login/')
          
           
    else:
        
        form = RegisterForm()
    
    context["form"]=form
    return render(request,'register.html',context)

def logoutUser(request):
    logout(request)
    return HttpResponse('<h1>looged out :) </h1>')
   
   
@login_required  
def profile(request):
    return render(request,'profile.html')
    