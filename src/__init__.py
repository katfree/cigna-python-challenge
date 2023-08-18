from src.file_importer import file_importer

def main():
    filepath = './python/data.csv'
    data = file_importer(filepath)
    print(data)
    return