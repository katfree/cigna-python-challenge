import csv
import os

from pprint import pprint

def detect_filetype(filepath):
    filename, file_extension = os.path.splitext(filepath)
    return file_extension


def file_importer(filepath):
    try:
        data = None
        filetype = detect_filetype(filepath)

        if filetype == '.csv':
            data = csv_loader(filepath)

        else:
            print(f'file with extention {filetype} is not supported.')

        return data
    
    except Exception as e:
        print(f'There was an error loading the file: {e}')
        

def csv_data_to_dict_list(csv_data):
    data = []
    headers = csv_data[0]

    for c in csv_data[1:]:
        csv_dict = {}
        
        for i, h in enumerate(headers):
            csv_dict[h] = c[i]        
            data.append(csv_dict)

    return data


def csv_loader(filepath):
    csv_data = []
    
    with open(filepath, newline='') as file:
        rows = csv.reader(file)    
        
        for row in rows:
            if len(row) > 0:
                csv_data.append(row)

    csv_dict = csv_data_to_dict_list(csv_data)
    return csv_dict