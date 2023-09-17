from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

# Create your views here.
def index(request):
    context = {
        "items": Item.objects.all(),
    }
    return render(request, "index.html", context)

def add(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:index")
    else:
        form = ItemForm()
    context = {
        "form": form,
        "items": Item.objects.all(),
    }
    return render(request, "add.html", context)