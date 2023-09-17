from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
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

def show_xml(request):
    items = Item.objects.all()
    data = serializers.serialize("xml", items)
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    items = Item.objects.all()
    data = serializers.serialize("json", items)
    return HttpResponse(data, content_type="application/json")

def show_xml_by_id(request, id):
    item = Item.objects.get(id=id)
    data = serializers.serialize("xml", [item])
    return HttpResponse(data, content_type="application/xml")

def show_json_by_id(request, id):
    item = Item.objects.get(id=id)
    data = serializers.serialize("json", [item])
    return HttpResponse(data, content_type="application/json")