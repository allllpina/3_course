from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Лаборатона робота 1. Виконав Чистяков Данило'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
