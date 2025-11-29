<<<<<<< HEAD
from django.shortcuts import render,redirect

from django.http import HttpResponse
from .forms import shoeForm
from .models import Shoe
=======
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ShoeForm 
>>>>>>> c09a507ea825e346f973d2081cb1d24e8ffa8931
# Create your views here.
def home(request): 
        return render(request, 'shoeAttic/home.html ')
# Create your views here.
def createShoe(request):
<<<<<<< HEAD
    form = shoeForm()
=======
    form = ShoeForm()
>>>>>>> c09a507ea825e346f973d2081cb1d24e8ffa8931

    if request.method == "POST":
        form = shoeForm(request.POST) # gets the data from what the user has input
        if form.is_valid():
            form.save()
            return redirect("readShoe")
    context = {"form": form}
<<<<<<< HEAD
    return render(request, "shoeAttic/forms.html", context)

def readShoe(request):
     shoes= Shoe.objects.all()
     context={"shoes":shoes}
     return render(request,"shoeAttic/shoes.html",context)

def shoe_detail(request, pk):
    shoes = Shoe.objects.get(id=pk)
    context={"shoes": shoes}
    return render(request, 'shoeAttic/shoe_detail.html',context)

def updateShoe(request, pk):

    shoe = Shoe.objects.get(id = pk )
    form = shoeForm(instance = shoe)

    if request.method == "POST":
        form = shoeForm(request.POST, instance= shoe)
        if form.is_valid():
            form.save()
            return redirect("readShoe")

    context = {"form": form}
    return render(request, "shoeAttic/forms.html", context)

def deleteShoe(request, pk):
    shoe = Shoe.objects.get(id = pk)

    if request.method == "POST":
        shoe.delete()
        return redirect("readShoe")
    context ={"shoes":shoe}
    return render(request, "shoeAttic/delete.html", context)
=======
    return render(request, "shoeAttic/forms.html", context)
>>>>>>> c09a507ea825e346f973d2081cb1d24e8ffa8931
