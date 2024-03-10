# This is where your application views are.

from django.shortcuts import render

def home(request):
   return render(request, "home.html", {})

def cars_view(request):
   return render(request, "cars.html", {})

def form_view(request):
   return render(request, "form.html", {})