from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "Yu-Gi-Oh! Card Collection",
        "name": "Muhammad Andhika Prasetya",
        "npm": "2206031302",
        "class": "PBP C",
    }
    return render(request, "index.html", context)