from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import listing


# Create your views here.
def home(request):
     return render(request, 'front/index.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['Title'] and request.POST['type'] and request.POST['location'] and request.POST['property_locality'] and request.FILES['icon'] and request.FILES['image1'] and request.FILES['image2'] and request.FILES['image3']:
            list = listing()
            list.Title = request.POST['Title']
            list.type = request.POST['type']
            list.location = request.POST['location']
            list.property_locality = request.POST['property_locality']



            list.icon = request.FILES['icon']
            list.image1 = request.FILES['image1']
            list.image2 = request.FILES['image2']
            list.image3 = request.FILES['image3']

            list.hunter = request.user
            list.save()
            return redirect('home')




        else :
             return render(request, 'front/create.html',{'error':'Please fill all the fields..!!'})

    else :
        return render(request, 'front/create.html')

def search(request):
    if request.method == 'GET':
        if request.GET['type'] and request.GET['location'] and request.GET['property_locality']:
            prop = listing()
            prop.type = request.GET['type']
            prop.location = request.GET['location']
            prop.property_locality = request.GET['property_locality']

            if request.GET['type'] == ('Flat')
                print('Hello')

        else:
             return render(request, 'front/index.html',{'error':'Please fill all the fields..!!'})

    else:
        return render(request, 'front/index.html')
