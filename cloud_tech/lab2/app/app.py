from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host='db',
            user = 'root',
            password = 'root',
            database = 'test_db'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'hello world'")
        message = cursor.fetchone()[0]
        conn.close() 
        return f'<h1>{message}</h1>'
    except Exception as e:
        return f'<h1>Помилка: {str(e)}</h1>'
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


