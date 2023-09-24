# invoices/urls.py
from django.urls import path
# from .views import InvoiceListCreateView, InvoiceRetrieveUpdateDestroyView, InvoiceDetailListCreateView, InvoiceDetailRetrieveUpdateDestroyView
from . views import *
urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/', InvoiceUpdateView.as_view(), name='invoice-detail'),
    path('invoice-details/', InvoiceDetailListCreateView.as_view(), name='invoice-detail-list'),
    path('invoice-details/<int:pk>/', InvoiceDetailUpdateView.as_view(), name='invoice-detail-detail'),
]
