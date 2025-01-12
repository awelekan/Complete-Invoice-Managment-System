from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'invoice_management'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/add/', views.add_invoice, name='add_invoice'),
    path('invoices/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('invoices/<int:pk>/edit/', views.edit_invoice, name='edit_invoice'),
    path('invoices/<int:pk>/delete/', views.delete_invoice, name='delete_invoice'),
    path('invoices/create/', views.create_invoice, name='create_invoice'),
    path('vendors/', views.vendor_list, name='vendor_list'),
    path('vendors/add/', views.add_vendor, name='add_vendor'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('vendors/<int:pk>/edit/', views.edit_vendor, name='edit_vendor'),
    path('vendors/<int:pk>/delete/', views.delete_vendor, name='delete_vendor'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:pk>/edit/', views.edit_customer, name='edit_customer'),
    path('customers/<int:pk>/delete/', views.delete_customer, name='delete_customer'),
    path('invoices/<int:pk>/pdf/', views.download_invoice_pdf, name='download_invoice_pdf'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
]
