from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User        #esko import karke hmlog form ka ek ek data means clean data ko database me save kar akte hain.
# Create your views here.


### This function will Add New Item and Show All Items...
def add_show(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
           ### fm.save()       #jab hmlogo kp all data save karna hua to eska use kar sakte hain.
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']  
            reg = User(name=nm, email=em, password=pw)  
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration() 

    stud = User.objects.all()   
    return render (request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})

### This Function Will Update/Edit...
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
                
    return render(request, 'enroll/updatestudent.html', {'form':fm}) 


### This Function will Delete the data...
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
