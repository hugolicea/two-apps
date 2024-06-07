# Data Visualization Web Application

This repository contains a collection of Python scripts and HTML templates for a web application that visualizes data using Google Charts, Chart.js, and Bootstrap. The application is built with Flask, a lightweight web framework for Python.

## Features

- **Flask Web Application**: The application is built with Flask, making it easy to run and deploy. Flask-Bootstrap is used to integrate Bootstrap with the Flask application.

- **Data Loading and Processing**: The Python script `data_loader.py` handles data loading and processing. It includes a function `load_json_to_chart_format` that loads data from a JSON file and converts it into a format suitable for Google Charts and Chart.js.

- **Web Page Templates**: The HTML templates, `graphs.html` and `app1.html`, are designed with Bootstrap for a responsive layout. They include elements like navigation bars, containers, and jumbotrons, and they use Bootstrap's grid system for layout management. The `graphs.html` file also includes Chart.js for creating interactive charts.

## Installation

The application requires Python and several Python packages. To install these packages, run the following command in your terminal:

```bash
pip install -r requirements.txt