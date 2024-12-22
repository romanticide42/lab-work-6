from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def init_connection():
    return sqlite3.connect('gifts.db')

@app.route('/gifts')
def get_gifts():
    try:
        conn = init_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM gifts')
        gifts = cursor.fetchall()

        return render_template('gifts.html', gifts=gifts)
    except Exception as e:
        return f'<font color="red"><h1> Ошибка: {str(e)}</h1></font>'
    finally:
        if conn:
            conn.close()

@app.route('/')
def index():
    return '<h1>Добро пожаловать!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
