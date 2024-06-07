import csv

from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from data_loader import load_csv_data, chart_load_json_data, d3_load_json_data, load_json_to_chart_format, load_csv_to_chart_format


home = Flask(__name__)
Bootstrap(home)


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/graphs')
def graphs():
    data = chart_load_json_data(
        'C:/Users/hugolicea/Documents/Local/Exercices/Python/two-apps/data/population.json')
    labels = data.columns.tolist()
    values = data.values.tolist()
    return render_template('graphs.html', labels=labels, values=values)


@home.route('/google_chart')
def google_chart():

    data = load_json_to_chart_format('C:/Users/hugolicea/Documents/Local/Exercices/Python/two-apps/data/population.json')
    data2 = load_csv_to_chart_format('C:/Users/hugolicea/Documents/Local/Exercices/Python/two-apps/data/colors.csv')
    data3 = load_csv_to_chart_format('C:/Users/hugolicea/Documents/Local/Exercices/Python/two-apps/data/sales.csv')

    return render_template('google_chart.html', data=data, data2=data2, data3=data3)
