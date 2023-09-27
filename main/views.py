from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .forms import ItemForm
from .models import Item
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
            return redirect("main:index")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Successfully logged in as " + user.username)
                return redirect("main:index")
        else:
            messages.info(request, "Username OR password is incorrect")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("main:index")