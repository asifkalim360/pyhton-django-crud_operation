from django.shortcuts import render, HttpResponseRedirect
from django.template import context
from .forms import StudentRegistration
from .models import User        #esko import karke hmlog form ka ek ek data means clean data ko database me save kar akte hain.
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Create your views here.


# ### This function will Add New Item and Show All Items...
# def add_show(request):
#     if request.method=='POST':
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#            ### fm.save()       #jab hmlogo kp all data save karna hua to eska use kar sakte hain.
#             nm = fm.cleaned_data['name']
#             em = fm.cleaned_data['email']
#             pw = fm.cleaned_data['password']  
#             reg = User(name=nm, email=em, password=pw)  
#             reg.save()
#             fm = StudentRegistration()
#     else:
#         fm = StudentRegistration() 

#     stud = User.objects.all()   
#     return render (request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})


### This function will Add New Item and Show All Items...
class UserAddShowView(TemplateView):
    template_name = "enroll/addandshow.html"
    def get_context_data(self, *args,**kwargs):         #GET REQUEST Method call
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration() 
        stud = User.objects.all()
        context = {'stu':stud, 'form':fm}
        return context

    def post(self, request):                        #POST REQUEST Method call 
        fm = StudentRegistration(request.POST)          
        if fm.is_valid():
           ### fm.save()       #jab hmlogo kp all data save karna hua to eska use kar sakte hain.
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']  
            reg = User(name=nm, email=em, password=pw)  
            reg.save()
            return HttpResponseRedirect('/')
        

### This Function Will Update/Edit...
# def update_data(request, id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(instance=pi)
                
#     return render(request, 'enroll/updatestudent.html', {'form':fm}) 



### This Class Will Update/Edit...
class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form':fm})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')      


### This Function will Delete the data...
# def delete_data(request, id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')


### This Class will Delete the data...
class UserDeleteView(RedirectView):
    url='/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)



