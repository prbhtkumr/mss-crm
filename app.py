from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Configuration
app.config['DATABASE_FILE'] = os.environ.get('DATABASE_FILE', 'database.db')

def get_db_connection():
    return sqlite3.connect(app.config['DATABASE_FILE'])

# Routes

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, company, address, phone, email FROM leads")
    users = cursor.fetchall()
    connection.close()
    return render_template('dashboard.html', users=users)
@app.route('/forms')
def show_form():
    return render_template('form.html')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        data = request.get_json()

        name = data.get('name')
        company = data.get('company')
        address = data.get('address')
        phone = data.get('phone')
        email = data.get('email')

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO leads (name, company, address, phone, email) VALUES (?, ?, ?, ?, ?)",
                       (name, company, address, phone, email))
        connection.commit()
        connection.close()

        return jsonify({'success': True})

    except Exception as e:
        # Log the exception
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
