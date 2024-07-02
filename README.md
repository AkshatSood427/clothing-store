# clothing-store
# Hi Fashion Garments Billing/Ordering System

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)


## Introduction
The Hi Fashion Garments Billing/Ordering System is a web application built using Flask and HTML. This application allows store personnel to manage orders and billing efficiently. It includes functionalities for creating new orders, viewing existing orders, and managing billing details.

## Features
- **Home Page**: Welcome page with buttons to navigate to New Order, View Orders, and Billing pages.
- **New Order**: Allows users to input customer name and order details. Items can be added dynamically and displayed in a table format with delete functionality.
- **View Orders**: Displays a list of all orders with options to view detailed information or delete orders.
- **Billing**: Allows users to input customer name and bill details. Items can be added dynamically and displayed in a table format with delete functionality. The total amount is calculated and displayed upon submission.

## Project Structure
clothing-store/
|-- home.py
|-- templates/
| |-- base.html
| |-- home.html
| |-- new_order.html
| |-- view_orders.html
| |-- order_details.html
| |-- billing.html
| |-- bill_details.html
|-- static/
|-- style.css


## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AkshatSood427/clothing-store.git
    cd clothing-store
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the application locally:

1. **Activate the virtual environment** (if not already activated):
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

2. **Run the Flask application**:
    ```bash
    python app.py
    ```

3. **Open your web browser** and navigate to `http://127.0.0.1:5000` to access the application.


