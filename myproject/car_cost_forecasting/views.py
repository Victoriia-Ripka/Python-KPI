from .index import CarPricePredictor
from .forms import ForecastForm
from django.shortcuts import render

def car_cost_view(request):
    if request.method == 'POST':
        form = ForecastForm(request.POST)
        # print(request.POST['latlaunch'], type(request.POST['latlaunch']))
        predicted_price = forecasting(request.POST)
        result = f'${str(predicted_price * 1000)[:2]},{str(predicted_price * 1000)[2:5]}'
        # print(predicted_price, '=', result)
    else:
        result = ''
        form = ForecastForm()

    data = {'form': form, 'result': result}

    return render(request, "forecast.html", data)
    # return render(request, 'forecast.html')

def forecasting(data):
    predictor = CarPricePredictor()
    predicted_price = predictor.predict_price(data['brand'], data['model'], data['esize'], data['power'], data['latlaunch'])
    return predicted_price
