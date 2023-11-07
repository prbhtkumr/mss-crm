from flask import Flask, render_template,request,jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('deprecated_dashboard.html')

DATABASE_FILE = 'database.db'

@app.route('/forms')
def show_form():
    return render_template('form.html')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()

    name = data.get('name')
    company = data.get('company')
    address = data.get('address')
    phone = data.get('phone')
    email = data.get('email')

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO leads (name, company, address, phone, email) VALUES (?, ?, ?, ?, ?)",
                   (name, company, address, phone, email))
    connection.commit()
    connection.close()

    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True)
