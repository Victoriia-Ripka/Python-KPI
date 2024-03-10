# This is where your application views are.

from django.shortcuts import render

def home(request):
   return render(request, "home.html", {})