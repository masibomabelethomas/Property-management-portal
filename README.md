# Property-management-portal
The Property Management Portal is a web application built using Django, a Python web framework, and Django REST Framework for creating APIs. This portal aims to provide a comprehensive solution for managing properties, tenants, leases, maintenance requests, payments, and invoices in a user-friendly manner.

Features:

Property Management: The portal allows users to add, view, and manage various properties. Each property contains attributes such as name, address, size, number of rooms, amenities, rental price, and status.

Tenant Management: Users can register and manage tenants associated with different properties. Tenant attributes include name, email, phone number, and the duration they will stay in the property.

Lease Management: The portal tracks lease agreements between properties and tenants. Each lease includes details such as start and end dates, rent amount, and reference to the tenant and property.

Maintenance Requests: Tenants can submit maintenance requests through the portal, and property managers can view and process these requests.

Payment Management: The portal allows users to track payments made by tenants for their rent. Each payment contains details like the payment amount, payment date, and reference to the tenant and property.

Invoice Generation: Invoices are automatically generated based on lease information and payment data, simplifying the process of tracking rental payments.

Authentication: The portal implements user authentication and permission control to secure sensitive data and restrict access to specific functionalities.

Usage:

Install Python and Django: Ensure you have Python and Django installed on your system.

Clone the Repository: Clone this repository to your local machine using Git.

Set Up Virtual Environment: Create and activate a virtual environment for the project.

Install Dependencies: Install required packages listed in the requirements.txt file.

Run Migrations: Perform database migrations using python manage.py migrate.

Create Superuser: Create a superuser account to access the Django admin panel.

Start the Server: Run the development server using python manage.py runserver.

Access the Portal: Navigate to the local development server address and access the Property Management Portal. Use the Django admin panel to manage data.

Contributing:
We welcome contributions to enhance the features and improve the portal's functionality. Feel free to submit pull requests or open issues to suggest improvements or report bugs.

License:
This project is open-source and available.

Contact:
For any questions or support, contact Thomas Masibo.

We hope this Property Management Portal helps you efficiently manage properties, tenants, and associated tasks. Happy property management!
