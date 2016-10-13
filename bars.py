import json

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as data_file:
        data_file = json.load(data_file, encoding='utf-8')
    return data_file


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
    data_file = load_data('D:/Бары.json')
    #pprint(data_file)
    print(get_biggest_bar(data_file))
    print(get_smallest_bar(data_file))
    longitude = int(input())
    latitude = int(input())
    print(get_closest_bar(data_file, longitude, latitude))
    #pprint(data_file[0])
    #print(data_file[0]['Cells']['SeatsCount'])
    #print(data_file[0].get('Number'))


