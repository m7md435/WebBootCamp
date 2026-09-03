from django.shortcuts import render
from django.views import View

def checkout(request):
    return render(request, 'payments/checkout.html')

def receipt(request, order_id):
    return render(request, 'payments/receipt.html', {'order_id': order_id})

class CheckoutView(View):
    def get(self, request):
        return render(request, 'payments/checkout.html')
    
    def post(self, request):
        return render(request, 'payments/receipt.html', {'order_id': 'ORD123456'})
