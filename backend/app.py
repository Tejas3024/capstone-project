from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS  # ← add this

app = Flask(__name__)
CORS(app)  # ← add this

# Create database table if not exists
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    return jsonify({"message": "Data saved successfully!"})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Backend is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
