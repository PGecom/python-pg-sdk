from django.shortcuts import render, redirect
from django.conf import settings
import pgrwpy
import random
import string
# Create your views here.


def create_ref_code():
    return 'REF-' + ''.join(random.choices(string.digits, k=5))


def index(request):
    return render(request, 'home.html', {})


def error(request):
    return render(request, 'error.html', {})

def success(request):
    return render(request, 'success.html', {})


def donate(request):
    if request.method == 'POST':
        client = pgrwpy.Client(
            auth=(settings.PG_USER_ID, settings.PG_SECRET_KEY), production_mode=False)
        amount = int(request.POST['amount'])
        data = {
            "amount": amount,
            "referenceId": create_ref_code(),
            "successUrl": "https://example.com",
            "errorUrl": "https://example.com"
        }
        payment = client.Payment.moncash(data)
        return redirect(payment['redirectUrl'])
    return render(request, 'donate.html', {})


def check_orderId(request):
    if request.method == 'POST':
        client = pgrwpy.Client(
            auth=(settings.PG_USER_ID, settings.PG_SECRET_KEY), production_mode=False)
        orderId = str(request.POST['orderId'])
        details = client.Payment.get_payment_details(orderId)
        print(details)
        redirect(success)
    return render(request, 'orderId.html', {})
