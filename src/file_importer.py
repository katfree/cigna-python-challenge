import csv
import os

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
        


def csv_loader(filepath):
    csv_data = []
    with open(filepath, newline='') as file:
        rows = csv.reader(file)    
        for row in rows:
            if len(row) > 0:
                csv_data.append(row)
    return csv_data