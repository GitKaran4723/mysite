from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/page2")
def home1():
    return render_template('home.html')

# Default port:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)