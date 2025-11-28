from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request): 
        return render(request, 'shoeAttic/home.html ')
# Create your views here.
def createMountain(request):
    form = ShoeForm()

    if request.method == "POST":
        form = ShoeForm(request.POST) # gets the data from what the user has input
        if form.is_valid():
            form.save()
            return redirect("readShoe")
            
    context = {"form": form}
    return render(request, "shoeAttic", context)