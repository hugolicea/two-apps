from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app2 = Flask(__name__)
Bootstrap(app2)


@app2.route('/')
def app2_home():
    return render_template('etl.html')

# Add more routes and functionalities for app2
