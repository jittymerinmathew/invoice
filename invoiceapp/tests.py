# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import Invoice, InvoiceDetail

# class InvoiceAPITestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.invoice_data = {
#             'date': '2023-09-24',
#             'customer_name': 'Test Customer'
#         }
#         self.invoice = Invoice.objects.create(**self.invoice_data)
#         self.invoice_detail_data = {
#             'invoice': self.invoice,
#             'description': 'Item 1',
#             'quantity': 2,
#             'unit_price': '10.00',
#             'price': '20.00'
#         }
#         self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

#     def test_create_invoice(self):
#         url = '/invoices/'
#         response = self.client.post(url, self.invoice_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Invoice.objects.count(), 2)

#     def test_update_invoice(self):
#         url = f'/invoices/{self.invoice.id}/'
#         updated_data = {'customer_name': 'Updated Customer'}
#         response = self.client.put(url, updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Invoice.objects.get(id=self.invoice.id).customer_name, 'Updated Customer')

#     def test_list_invoices(self):
#         url = '/invoices/'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_retrieve_invoice(self):
#         url = f'/invoices/{self.invoice.id}/'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_invoice_detail(self):
#         url = '/invoice-details/'
#         response = self.client.post(url, self.invoice_detail_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(InvoiceDetail.objects.count(), 2)

#     def test_list_invoice_details(self):
#         url = '/invoice-details/'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_retrieve_invoice_detail(self):
#         url = f'/invoice-details/{self.invoice_detail.id}/'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
