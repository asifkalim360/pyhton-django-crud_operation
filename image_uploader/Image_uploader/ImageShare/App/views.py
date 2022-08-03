from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Form

# Create your views here.

def index(request):
    ### SINGLE OBJECT...
    # form = Form.objects.get(title='css3')
    # form = Form.objects.get(id=3)
    # ### ACCESSING THE OBJECT DATA...
    # print(form.title)
    # print(form)

    ### ACCESSING MULTIPLE OBJECTS DATA...
    form = Form.objects.all()
    print(form)
    #return HttpResponse('hello world!')
    return render(request, 'index.html',{'form':form, 'name':"Asif", 'list':[1,2,3,4,5,6]})


def about(request):
    #return HttpResponse('This is about page!')
    return render(request, 'about.html')

def upload(request):
    #return HttpResponse('this is contact page!')  
    if request.method == 'POST':
        image_title=request.POST['title']
        image = request.FILES['image']
        form = Form.objects.create(title=image_title, image=image)
        if form:
            return HttpResponseRedirect('/')
    return render(request, 'upload.html')      
