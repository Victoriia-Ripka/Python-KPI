from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
   return render(request, "home.html", {})


def home(request):
   return HttpResponse("Hello, this is the home page.")


def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)