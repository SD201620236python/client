from flask import Flask

app = Flask(__name__)

@app.route('/info')
def print_hi():
    return('/info.json')

def main():
    app.run('127.0.1.0', '5000')

