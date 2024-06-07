import csv
import json
import pandas as pd


def d3_load_json_data(file_path):
    data = pd.read_json(file_path)
    return data.to_dict(orient='records')


def chart_load_json_data(file_path):
    data = pd.read_json(file_path)
    return data


def load_csv_data(file_path):
    data = pd.read_csv(file_path)
    return data


def load_json_to_chart_format(json_file_path):
    # Load data from a JSON file
    with open(json_file_path) as f:
        raw_data = json.load(f)

    # Convert the data to the format expected by Google Charts
    # Get the keys from the first dictionary to use as headers
    data = [list(raw_data[0].keys())]
    for item in raw_data:
        # Convert numerical data to integers or floats
        converted_values = [int(value) if str(value).isdigit() else float(value) if str(
            value).replace('.', '', 1).isdigit() else value for value in item.values()]
        # Append the values of each dictionary as a new row
        data.append(converted_values)

    return data


def load_csv_to_chart_format(csv_file_path):
    # Load data from a CSV file
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        raw_data = list(reader)

    # Convert the data to the format expected by Google Charts
    # The first row of the CSV file is used as headers
    data = [raw_data[0]]
    for row in raw_data[1:]:
        # Convert numerical data to integers or floats
        converted_row = [int(value) if value.isdigit() else float(
            value) if value.replace('.', '', 1).isdigit() else value for value in row]
        # Append each row as a new row in the chart data
        data.append(converted_row)

    return data
