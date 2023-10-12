from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from .forms import ItemForm
from .models import Item, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        items = Item.objects.filter(user=request.user)
    else:
        items = []
    context = {
        "items": items,
    }
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def add(request):
    if request.method == "POST":
        data = request.POST.copy()
        data["user"] = request.user.id
        form = ItemForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:index")
        else:
            print(form.errors)
            messages.error(request, "Invalid form")
    return render(request, "add.html")
        

@login_required(login_url="/login/")
def show_xml(request):
    items = Item.objects.filter(user=request.user)
    data = serializers.serialize("xml", items)
    return HttpResponse(data, content_type="application/xml")

@login_required(login_url="/login/")
def show_json(request):
    items = Item.objects.filter(user=request.user)
    data = serializers.serialize("json", items)
    return HttpResponse(data, content_type="application/json")

@login_required(login_url="/login/")
def show_xml_by_id(request, id):
    item = Item.objects.get(id=id)
    if item.user != request.user:
        return redirect("main:index")
    data = serializers.serialize("xml", [item])
    return HttpResponse(data, content_type="application/xml")

@login_required(login_url="/login/")
def show_json_by_id(request, id):
    item = Item.objects.get(id=id)
    if item.user != request.user:
        return redirect("main:index")
    data = serializers.serialize("json", [item])
    return HttpResponse(data, content_type="application/json")

def register(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, "Successfully registered as " + username)
                return redirect("main:login")
            else:
                messages.info(request, "Username already exists")
        else:
            messages.info(request, "Passwords do not match")
    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            request.session["last_login"] = str(timezone.now())
            messages.info(request, "Successfully logged in as " + username)
            return redirect("main:index")
        else:
            messages.info(request, "Invalid credentials")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    request.session.flush()
    return redirect("main:index")

@login_required(login_url="/login/")
def add_amount(request, id):
    item = Item.objects.get(id=id)
    if item.user == request.user:
        item.amount += 1
        item.save()
        return redirect("main:index")
    return render(request, "index.html")

@login_required(login_url="/login/")
def reduce_amount(request, id):
    item = Item.objects.get(id=id)
    if item.user == request.user:
        item.amount -= 1
        item.save()
        return redirect("main:index")
    return render(request, "index.html")

@login_required(login_url="/login/")
def delete(request, id):
    item = Item.objects.get(id=id)
    if item.user == request.user:
        item.image.delete()
        item.delete()
        return redirect("main:index")
    return render(request, "index.html")

@login_required(login_url="/login/")
def delete_all(request):
    items = Item.objects.filter(user=request.user)
    for item in items:
        item.image.delete()
    items.delete()
    return render(request, "index.html")

@login_required(login_url="/login/")
def get_items_json(request):
    items = Item.objects.filter(user=request.user)
    data = serializers.serialize("json", items)
    return HttpResponse(data, content_type="application/json")

@login_required(login_url="/login/")
def create_item_ajax(request):
    if request.method == "POST":
        new_item = Item.objects.create(
            user=request.user,
            name=request.POST["name"],
            amount=request.POST["amount"],
            description=request.POST["description"],
            card_type=request.POST["card_type"],
            passcode=request.POST["passcode"],
            attribute=request.POST["attribute"],
            types=request.POST["types"],
            level=request.POST["level"],
            atk=request.POST["atk"],
            deff=request.POST["deff"],
            effect_type=request.POST["effect_type"],
            card_property=request.POST["card_property"],
            rulings=request.POST["rulings"],
            image=request.FILES["image"]
        )
        new_item.save()
        return HttpResponse('Card added successfully', status=201)
    return HttpResponseNotFound()

@login_required(login_url="/login/")
def delete_item_ajax(request, id):
    if request.method == "DELETE":
        item = Item.objects.get(id=id)
        if item.user == request.user:
            item.delete()
            return HttpResponse("Card deleted successfully", status=204)
        return HttpResponse("You are not allowed to delete this card", status=403)
    return HttpResponseNotFound()
