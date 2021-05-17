# Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON.
import pickle
import json
products = ['Notebooks', 'Books', 'Smartphones', 'Headphones', 'Playstation']
pickle_products = pickle.dumps(products)
with open('json_file.json', 'w') as json_file:
    json.dump(str(pickle_products), json_file)
