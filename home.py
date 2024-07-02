from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

orders = []
bills = []
order_id_counter = 1

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new_order', methods=['GET', 'POST'])
def new_order():
    global order_id_counter
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        order_details = request.form.getlist('order_details')
        new_order = {
            'id': order_id_counter,
            'customer_name': customer_name,
            'details': [item.split('|') for item in order_details]
        }
        orders.append(new_order)
        order_id_counter += 1
        return redirect(url_for('view_orders'))
    return render_template('new_order.html')

@app.route('/view_orders')
def view_orders():
    return render_template('view_orders.html', orders=orders)

@app.route('/order/<int:order_id>')
def view_order(order_id):
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        return render_template('order_details.html', order=order)
    return redirect(url_for('view_orders'))

@app.route('/delete_order/<int:order_id>')
def delete_order(order_id):
    global orders
    orders = [order for order in orders if order['id'] != order_id]
    return redirect(url_for('view_orders'))

@app.route('/billing', methods=['GET', 'POST'])
def billing():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        bill_details = request.form.getlist('bill_details')
        new_bill = {
            'customer_name': customer_name,
            'details': [item.split('|') for item in bill_details]
        }
        bills.append(new_bill)
        return render_template('bill_details.html', bill=new_bill)
    return render_template('billing.html')

if __name__ == '__main__':
    app.run(debug=True)
