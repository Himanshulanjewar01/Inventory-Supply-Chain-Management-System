import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_FILE = 'inventory.db'

def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/dashboard')
def dashboard():
    db = get_db()
    # Complex SQL join to get product metrics along with supplier details
    query = """
        SELECT p.product_id, p.product_name, p.stock_quantity, p.unit_price, 
               p.min_threshold, s.company_name 
        FROM products p
        LEFT JOIN suppliers s ON p.supplier_id = s.supplier_id
    """
    inventory_items = db.execute(query).fetchall()
    db.close()
    return render_template('dashboard.html', items=inventory_items)

@app.route('/restock', methods=['POST'])
def restock_product():
    product_id = request.form['product_id']
    added_qty = int(request.form['quantity'])
    
    db = get_db()
    db.execute("UPDATE products SET stock_quantity = stock_quantity + ? WHERE product_id = ?", (added_qty, product_id))
    db.commit()
    db.close()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
