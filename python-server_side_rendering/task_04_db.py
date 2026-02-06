from flask import Flask, render_template, request, jsonify
import json
import csv
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open ('items.json', 'r') as file:
        data = json.load(file)
        values = data.get('items', [])
        return render_template('items.html', items=values)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products =[]
    if source == 'json':
        with open ('products.json', 'r') as file:
            products = json.load(file)

    elif source == 'csv':
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row['id']),
                    "name": row['name'],
                    "category": row['category'],
                    "price": float(row['price'])
                })
    
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            for row in rows:
                products.append({
                    "id": row[0],
                    "name": row[1],
                    "category": row[2],
                    "price": row[3]
                })
            conn.close()
        except Exception:
            return render_template('products_display.html', error="Database error")

    else:
        return "Wrong source"
    if product_id:
            products = [product for product in products if str(product['id']) == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        
    return render_template('product_display.html', products=products)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
