from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def login(request):
    return render(request,'index.html')
@csrf_protect
def log(request):
    if  request.method =='POST':
        name=request.POST['user']
        passw=request.POST['pass']
        user=auth.authenticate(username=name,password=passw)
        if user is not None:
            auth.login(request,user)
            return render(request,'log.html')
        else:
            messages.info(request,'invalid user')
            return redirect("login")
    else:
        return render(request,'index.html')
   

def classinfo(request):
    if request.method=='POST':
     
        if request.POST['option']=='LKG':
            if request.POST['section']=='A':
                names=[{'name':'Maran','roll':101},{'name':'Adithya','roll':102},{'name':'Shiva','roll':103}]
            if request.POST['section']=='B':
                names=[{'name':'Manoj','roll':201},{'name':'Thamil','roll':202},{'name':'Dharani','roll':203}]
            if request.POST['section']=='C':
                names=[{'name':'Dharun','roll':301},{'name':'Praveen','roll':302},{'name':'Muruga','roll':303}]
            return render(request,'log.html',context={'names':names})
       
                
            
        
    