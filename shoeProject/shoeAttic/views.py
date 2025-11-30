from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import shoeForm
from .models import Shoe

# Home view
def home(request):
    return render(request, 'shoeAttic/home.html')

# Create view
def createShoe(request):
    form = ShoeForm()
    if request.method == "POST":
        form = ShoeForm(request.POST)  # gets the data from what the user has input
        if form.is_valid():
            form.save()
            return redirect("readShoe")
    context = {"form": form}
    return render(request, "shoeAttic/forms.html", context)

# Read view
def readShoe(request):
    shoes = Shoe.objects.all()
    context = {"shoes": shoes}
    return render(request, "shoeAttic/shoes.html", context)

# Detail view
def shoe_detail(request, pk):
    shoe = Shoe.objects.get(id=pk)
    context = {"shoe": shoe}
    return render(request, 'shoeAttic/shoe_detail.html', context)

# Update view
def updateShoe(request, pk):
    shoe = Shoe.objects.get(id=pk)
    form = ShoeForm(instance=shoe)

    if request.method == "POST":
        form = ShoeForm(request.POST, instance=shoe)
        if form.is_valid():
            form.save()
            return redirect("readShoe")

    context = {"form": form}
    return render(request, "shoeAttic/forms.html", context)

# Delete view
def deleteShoe(request, pk):
    shoe = Shoe.objects.get(id=pk)

    if request.method == "POST":
        shoe.delete()
        return redirect("readShoe")

    context = {"shoe": shoe}
    return render(request, "shoeAttic/delete.html", context)