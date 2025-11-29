from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ShoeForm 
# Create your views here.
def home(request): 
        return render(request, 'shoeAttic/home.html ')
# Create your views here.
def createShoe(request):
    form = ShoeForm()

    if request.method == "POST":
        form = ShoeForm(request.POST) # gets the data from what the user has input
        if form.is_valid():
            form.save()
            return redirect("readShoe")
            
    context = {"form": form}
    return render(request, "shoeAttic/forms.html", context)