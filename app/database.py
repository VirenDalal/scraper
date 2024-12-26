import json
from app.models import Product

class Database:
    def save_products(self, products: list[Product]) -> int:
        raise NotImplementedError

class JSONDatabase(Database):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_products(self, products: list[Product]) -> int:
        with open(self.file_path, 'r+') as json_file:
            try:
                 existing_data = json.load(json_file)
            except json.JSONDecodeError:
                existing_data = []
            for data in products:
                existing_data.append(data)  # Append the new data
            json_file.seek(0)  # Go to the beginning of the file
            json.dump(existing_data, json_file, indent=4)


