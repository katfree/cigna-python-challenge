from src.file_importer import file_importer

def main():
    filepath = './python/data.csv'
    file_data = file_importer(filepath)
    
    return