# *-* coding: utf-8 -*-
import json
import os
import sys

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as data_file:
            return json.load(data_file)


def get_biggest_bar(data):
    return max(data, key=lambda item:item['Cells']['SeatsCount'])['Cells']['Name']

def get_smallest_bar(data):
    return min(data, key=lambda item:item['Cells']['SeatsCount'])['Cells']['Name']


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda item:((item['Cells']['geoData']['coordinates'][0]-longitude)**2\
                               +(item['Cells']['geoData']['coordinates'][1]-latitude)**2)**0.5)['Cells']['Name']




if __name__ == '__main__':
    if len(sys.argv) == 1:
        bars_json_data_file = load_data(input("Enter path to your Bars.json file: "))
    else:
        bars_json_data_file = load_data(sys.argv[1])
    print("The biggest bar:", get_biggest_bar(bars_json_data_file))
    print("The smallest bar:", get_smallest_bar(bars_json_data_file))
    try:
        longitude = float(input("Enter your current longitude: "))
        latitude = float(input("Enter your current latitude: "))
    except ValueError:
        longitude = None
        latitude = None

    if longitude is None:
        print("Wtf, dude?")
    elif latitude is None:
        print("Wtf, dude?")
    else:
        print("The closest bar to you:", get_closest_bar(bars_json_data_file, longitude, latitude))



