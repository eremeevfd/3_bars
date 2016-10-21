# *-* coding: utf-8 -*-
import json
import os
import sys

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as data_file:
            return json.load(data_file)


def get_biggest_bar(data):
    max = 0
    bar = ""
    for i in data:
        if i['Cells']['SeatsCount'] > max:
            max = i['Cells']['SeatsCount']
            bar = i['Cells']['Name']
    return bar

def get_smallest_bar(data):
    min = 1000
    bar = ""
    for i in data:
        if i['Cells']['SeatsCount'] < min:
            min = i['Cells']['SeatsCount']
            bar = i['Cells']['Name']
    return bar


def get_closest_bar(data, longitude, latitude):
    long = 1000
    lat = 1000
    bar = ""
    for i in data:
        if i['Cells']['geoData']['coordinates'][0] - longitude < long and \
            i['Cells']['geoData']['coordinates'][1] - latitude < lat:
                bar = i['Cells']['Name']
    return bar




if __name__ == '__main__':
    if len(sys.argv) == 1:
        data_file = load_data(os.path.join(".", "Бары.json"))
    else:
        data_file = load_data(sys.argv[1])
    print("Самый большой бар:", get_biggest_bar(data_file))
    print("Самый маленький бар:", get_smallest_bar(data_file))
    longitude = int(input("Введите Вашу долготу: "))
    latitude = int(input("Введите Вашу широту: "))
    print("Ближайший к вам бар:", get_closest_bar(data_file, longitude, latitude))



