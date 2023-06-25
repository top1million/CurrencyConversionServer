from django.http import HttpResponse
from django.template import loader
from .models import CurrencyConversionRate
from django.shortcuts import render
import requests

api_key = "34ba08f8907e96e96067390b"

def main(request):
    return render(request, "main.html")

def convert(request):
    from_currency = request.POST["from"]
    to_currency = request.POST["to"]
    amount = request.POST["amount"]
    #https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/EUR/GBP
    api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    response = requests.get(api_url)
    """
    {
	"result": "success",
	"documentation": "https://www.exchangerate-api.com/docs",
	"terms_of_use": "https://www.exchangerate-api.com/terms",
	"time_last_update_unix": 1585267200,
	"time_last_update_utc": "Fri, 27 Mar 2020 00:00:00 +0000",
	"time_next_update_unix": 1585270800,
	"time_next_update_utc": "Sat, 28 Mar 2020 01:00:00 +0000",
	"base_code": "EUR",
	"target_code": "GBP",
	"conversion_rate": 0.8412
}
    """
    if response.status_code != 200:
        return HttpResponse(f"An error occured: {response.status_code}")
    data = response.json()
    rate = data["conversion_rate"]
    converted_amount = float(amount) * float(rate)
    context = {
        "from_currency": from_currency,
        "to_currency": to_currency,
        "amount": amount,
        "converted_amount": converted_amount,
        "rate": rate,
    }
    return render(request, "main.html", context)


