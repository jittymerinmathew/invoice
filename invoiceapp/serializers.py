# invoices/serializers.py
from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = InvoiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'
    
    def to_representation(self, instance):
        """
        Custom method to serialize the Invoice object.
        """
        representation = super(InvoiceSerializer, self).to_representation(instance)
        # You can customize how the Invoice object is represented here
        # For example, convert a date field to a string:
        representation['date'] = instance.date.strftime('%Y-%m-%d')
        return representation
