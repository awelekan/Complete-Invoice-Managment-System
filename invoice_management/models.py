from django.db import models
from django.contrib.auth.models import User

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

# Invoice Model
class Invoice(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Overdue', 'Overdue'),
    ])
    installment_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer.name}"

# Installment Payment Model
class InstallmentPayment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='installments')
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Installment Payment {self.id} for Invoice {self.invoice.id}"

# Vendor Model
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='vendors')
    logo = models.ImageField(upload_to='vendor_logos/', null=True, blank=True)

    def __str__(self):
        return self.name

# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    preferred_payment_method = models.CharField(max_length=50, choices=[
        ('Bank Transfer', 'Bank Transfer'),
        ('Credit Card', 'Credit Card'),
        ('PayStack', 'PayStack'),
    ])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='customers')
    image = models.ImageField(upload_to='customer_images/', null=True, blank=True)

    def __str__(self):
        return self.name

# Payment Model
class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('Bank Transfer', 'Bank Transfer'),
        ('Credit Card', 'Credit Card'),
        ('PayStack', 'PayStack'),
    ])

    def __str__(self):
        return f"Payment for Invoice {self.invoice.id}"

# Audit Log Model
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"