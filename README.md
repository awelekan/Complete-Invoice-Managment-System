# Kanzulgina Invoice Management System

Kanzulgina Invoice Management System is a Django-based web application designed to manage invoices, vendors, customers, and products. The system allows users to create, edit, and delete invoices, vendors, and customers, as well as generate PDF invoices.

## Features

- User authentication (login, logout, register)
- Dashboard with an overview of invoices, vendors, and customers
- CRUD operations for invoices, vendors, customers, and categories
- Generate PDF invoices
- Responsive design with a clean and modern interface

## Installation

### Prerequisites

- Python 3.x
- Django 3.x
- Virtual environment (recommended)

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/kanzulgina_invoice.git
   cd kanzulgina_invoice

2. Create and activate a virtual environment:
   python -m venv venv
# On Windows
.\venv\Scripts\activate

3. Install the dependencies:
   pip install -r requirements.txt

4. Apply migrations:  python manage.py makemigrations
python manage.py migrate
   
5. python manage.py makemigrations
python manage.py migrate

6. Create a superuser:
 python manage.py createsuperuser

   
7. Run the development server:
    python manage.py runserver

8. Access the application:
Open your web browser and go to http://127.0.0.1:8000/


Features / Usage

Authentication
Login: Access the login page at /login/ and enter your credentials.
Register: Access the registration page at /register/ to create a new account.
Logout: Click the logout link in the navigation menu to log out.

Dashboard
The dashboard provides an overview of invoices, vendors, and customers.
Access the dashboard at /.

Invoices
List Invoices: Access the list of invoices at /invoices/.
Add Invoice: Create a new invoice at /invoices/add/.
Edit Invoice: Edit an existing invoice at /invoices/<int:pk>/edit/.
Delete Invoice: Delete an invoice at /invoices/<int:pk>/delete/.
Generate PDF: Generate a PDF for an invoice at /invoices/<int:pk>/pdf/.

Vendors
List Vendors: Access the list of vendors at /vendors/.
Add Vendor: Create a new vendor at /vendors/add/.
Edit Vendor: Edit an existing vendor at /vendors/<int:pk>/edit/.
Delete Vendor: Delete a vendor at /vendors/<int:pk>/delete/.

Customers
List Customers: Access the list of customers at /customers/.
Add Customer: Create a new customer at /customers/add/.
Edit Customer: Edit an existing customer at /customers/<int:pk>/edit/.
Delete Customer: Delete a customer at /customers/<int:pk>/delete/.

Categories
List Categories: Access the list of categories at /categories/.
Add Category: Create a new category at /categories/create/.
Edit Category: Edit an existing category at /categories/<int:pk>/update/.
Delete Category: Delete a category at /categories/<int:pk>/delete/.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Django
xhtml2pdf
