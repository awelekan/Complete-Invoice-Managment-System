from django import forms
from .models import Invoice, Vendor, Customer, Category, Product, InstallmentPayment

class InvoiceForm(forms.ModelForm):
    installment_payment = forms.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2,
        help_text="Optional: Enter installment payment amount"
    )

    class Meta:
        model = Invoice
        fields = ['customer', 'vendor', 'product', 'issue_date', 'due_date', 'total_amount', 'status', 'installment_payment']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        if product:
            cleaned_data['total_amount'] = product.price
        return cleaned_data

class InstallmentPaymentForm(forms.ModelForm):
    class Meta:
        model = InstallmentPayment
        fields = ['invoice', 'payment_date', 'amount']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'contact_email', 'phone_number', 'address', 'category', 'products', 'logo']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact_email', 'phone_number', 'address', 'preferred_payment_method']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'image']