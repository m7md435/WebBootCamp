from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('receipt/<str:order_id>/', views.receipt, name='receipt'),
]
