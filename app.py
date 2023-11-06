from flask import Flask, render_template,request,jsonify
import sqlite3

app = Flask(__name__)

# Route to serve the HTML dashboard file
@app.route('/')
def index():
    return render_template('deprecated_dashboard.html')

# Database connection
DATABASE_FILE = 'database.db'

# Route to render the form page
@app.route('/forms')
def show_form():
    return render_template('form.html')

# Route to handle form submission and add customer to the leads table
@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()

    # Extract data from the JSON payload
    name = data.get('name')
    company = data.get('company')
    address = data.get('address')
    phone = data.get('phone')
    email = data.get('email')

    # Insert the data into the leads table
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO leads (name, company, address, phone, email) VALUES (?, ?, ?, ?, ?)",
                   (name, company, address, phone, email))
    connection.commit()
    connection.close()

    # Send success response
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True)
