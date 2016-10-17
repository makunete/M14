from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/calendari/')
def calend(name=None):
    return render_template('calendari.html', name=name)

if __name__ == "__main__":
    app.run()
