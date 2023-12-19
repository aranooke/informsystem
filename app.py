from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Функция для создания подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('cinema.db')
    conn.row_factory = sqlite3.Row
    return conn

# Функция для выполнения запросов к базе данных
def execute_query(query, params=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employees')
def employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    data = cursor.fetchall()
    conn.close()
    return render_template('employees.html', data=data)

@app.route('/sold_tickets')
def sold_tickets():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Repertoire JOIN Places ON Repertoire.session_code = Places.session_code')
    data = cursor.fetchall()
    conn.close()
    return render_template('sold_tickets.html', data=data)

@app.route('/free_places')
def free_places():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Repertoire JOIN Places ON Repertoire.session_code = Places.session_code WHERE Places.place IS NULL')
    data = cursor.fetchall()
    conn.close()
    return render_template('free_places.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
