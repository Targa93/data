from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"<h1>Сьогоднішня дата: {current_date}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
