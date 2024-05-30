from django.shortcuts import render

def car_cost_view(request):
    return render(request, 'forecast.html')
