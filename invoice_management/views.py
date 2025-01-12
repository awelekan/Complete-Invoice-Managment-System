from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Invoice, Vendor, Customer, Category, Product, InstallmentPayment
from .forms import InvoiceForm, VendorForm, CustomerForm, CategoryForm, ProductForm, InstallmentPaymentForm
from django.template.loader import get_template
from xhtml2pdf import pisa

# Authentication Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('invoice_management:dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('invoice_management:login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('invoice_management:dashboard')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'authentication/register.html')

# Dashboard View
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('invoice_management:login')
    
    invoices = Invoice.objects.all()
    vendors = Vendor.objects.all()
    customers = Customer.objects.all()
    context = {
        'invoices': invoices,
        'vendors': vendors,
        'customers': customers
    }
    return render(request, 'dashboard/dashboard.html', context)

# Invoice Views
@login_required
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice_management/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    installments = InstallmentPayment.objects.filter(invoice=invoice)
    return render(request, 'invoices/invoice_detail.html', {'invoice': invoice, 'installments': installments})

@login_required
def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'invoice_management/create_invoice.html', {'form': form})

@login_required
def delete_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_management:invoice_list')
    return render(request, 'invoice_management/delete_invoice.html', {'invoice': invoice})

@login_required
def download_invoice_pdf(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    template_path = 'invoice_management/invoice_pdf.html'
    context = {'invoice': invoice}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'invoice_management/add_invoice.html', {'form': form})

@login_required
def edit_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:invoice_list')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoice_management/edit_invoice.html', {'form': form})

# Installment Payment Views
@login_required
def add_installment_payment(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == 'POST':
        form = InstallmentPaymentForm(request.POST)
        if form.is_valid():
            installment = form.save(commit=False)
            installment.invoice = invoice
            installment.save()
            return redirect('invoice_management:invoice_detail', pk=invoice.id)
    else:
        form = InstallmentPaymentForm(initial={'invoice': invoice})
    return render(request, 'installments/installment_form.html', {'form': form, 'invoice': invoice})

# Vendor Views
@login_required
def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'invoice_management/vendor_list.html', {'vendors': vendors})

@login_required
def create_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:vendor_list')
    else:
        form = VendorForm()
    return render(request, 'invoice_management/create_vendor.html', {'form': form})

@login_required
def delete_vendor(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_list')
    return render(request, 'invoice_management/delete_vendor.html', {'vendor': vendor})

@login_required
def add_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:vendor_list')
    else:
        form = VendorForm()
    return render(request, 'invoice_management/add_vendor.html', {'form': form})

@login_required
def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'invoice_management/vendor_detail.html', {'vendor': vendor})

@login_required
def edit_vendor(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:vendor_list')
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'invoice_management/edit_vendor.html', {'form': form})

# Customer Views
@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'invoice_management/customer_list.html', {'customers': customers})

@login_required
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'create_customer.html', {'form': form})

@login_required
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('invoice_management:customer_list')
    return render(request, 'invoice_management/delete_customer.html', {'customer': customer})

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'invoice_management/add_customer.html', {'form': form})

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'invoice_management/customer_detail.html', {'customer': customer})

@login_required
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'invoice_management/edit_customer.html', {'form': form})

# Category Views
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('invoice_management:category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})

# Product Views
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('invoice_management:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('invoice_management:product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

# Customer Dashboard
@login_required
def customer_dashboard(request):
    customer = get_object_or_404(Customer, user=request.user)
    products = customer.products.all()
    return render(request, 'customers/customer_dashboard.html', {'customer': customer, 'products': products})

# Vendor Dashboard
@login_required
def vendor_dashboard(request):
    vendor = get_object_or_404(Vendor, user=request.user)
    products = vendor.products.all()
    return render(request, 'vendors/vendor_dashboard.html', {'vendor': vendor, 'products': products})

# Subscribe to Product
@login_required
def subscribe_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_customer:
        customer = get_object_or_404(Customer, user=request.user)
        customer.products.add(product)
    elif request.user.is_vendor:
        vendor = get_object_or_404(Vendor, user=request.user)
        vendor.products.add(product)
    return redirect('invoice_management:dashboard')