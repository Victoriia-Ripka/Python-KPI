# This is where your application views are.

from django.shortcuts import render
from django.views import View
from django.http import Http404
from .models import Car
from .forms import CarForm
from .models import Car
import pandas as pd

def home(request):
   return render(request, "home.html", {})

def cars_view(request):
   cars = ["fiat", 'ford', 'volvo', 'audi', 'mazda', 'bmw', 'toyota']
   data = {
      "km": [20310, 12780, 40678, 15689, 25643, 38734, 30876],
      "h": [389, 200, 589, 248, 345, 489, 512],
      'l/100km': [9.5, 10, 12, 7.5, 13, 8, 10.8],
      "year": [2002, 2013, 2018, 2015, 2020, 2014, 2019],
      "date": ['2020/12/01', '2020/12/01', '2020/12/01', '2022/12/01', '2022/12/01', '2022/12/01', '2023/01/15']
   }

   df = pd.DataFrame(data, index=cars)
   
   return render(request, "cars.html", {"df": df})

def form_view(request):
   cars = ["fiat", 'ford', 'volvo', 'audi', 'mazda', 'bmw', 'toyota']
   form = CarForm(car_models=cars)
   return render(request, "form.html", {'form': form})

# class CarDetailView(View):
#     template_name = 'car_detail.html'

#     def get(self, request, car_slug):
#         try:
#             car = Car.objects.get(slug=car_slug)
#         except Car.DoesNotExist:
#             raise Http404("Car does not exist")

#         return render(request, self.template_name, {'car': car})