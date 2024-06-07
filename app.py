from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app1 = Flask(__name__)
Bootstrap(app1)


@app1.route('/')
def app1_home():
    return render_template('app1.html')

# Add more routes and functionalities for app1
