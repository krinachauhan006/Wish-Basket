# 🎁 Wish Basket – Personalized Gift Shopping System

Wish Basket is a web-based gift shopping management system developed using **Python and Django**. It is designed to organize personalized gift products and manage essential shopping activities, including carts, orders, payments, wishlists, and customer reviews.

## ✨ Features

- **User Management:** Manage user accounts and profile information.
- **Location Management:** Maintain country, state, and city details.
- **Gift Categories:** Organize gifts into different categories.
- **Gift Items:** Store and manage personalized gift product information.
- **Shopping Cart:** Manage products added to the cart.
- **Order Management:** Maintain customer orders and order statuses.
- **Payment Management:** Store payment details and transaction-related information.
- **Wishlist:** Maintain a list of desired gift items.
- **Reviews & Ratings:** Manage customer feedback and product ratings.
- **Contact Us:** Store customer inquiries and communication details.
- **Admin Panel:** Manage application data using Django Admin, including customized filters and theme settings.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application framework |
| SQLite | Database management |
| HTML | Web page structure |
| CSS | Styling and presentation |
| Django Admin | Administrative data management |

## 🏗️ Key Django Concepts Implemented

- Django MVT (Model-View-Template) Architecture
- Database Models and Relationships
- ForeignKey Relationships
- CRUD (Create, Read, Update, Delete) Operations
- Choice Fields
- Database Migrations
- Django Admin Panel Customization

## ⚙️ Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/krinachauhan006/Wish-Basket.git
```

2. Navigate to the project directory:

```bash
cd Wish-Basket
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Create a Django superuser:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open the application in your browser:

```text
http://127.0.0.1:8000/
```

**Note:** The commands assume that `manage.py` and `requirements.txt` are located in the repository root. Adjust the directory or setup steps if your project structure differs.

## 🎯 Project Objective

The objective of Wish Basket is to apply Django concepts to develop a structured, database-driven gift shopping management application while understanding how different models and relationships work together in a web application.

## 📌 Project Background

Developed as the final project during the Python and Django Summer Internship at **Infolabz IT Services Pvt. Ltd.** (July 2026).

---

**Developed using Python and Django.**
