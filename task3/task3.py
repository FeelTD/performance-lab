import json
import pandas as pd


def replace_item(obj, key, dict_pairs):
    for k, v in obj.items():
        if isinstance(v, dict):
            obj[k] = replace_item(v, key, dict_pairs)
        elif isinstance(v, list):
            for every in v:
                replace_item(every, key, dict_pairs)
    for k, v in dict_pairs.items():
        if key in obj and obj['id'] == k:
            obj[key] = v
    return obj


values_path = input("Введите путь к файлу values.json")  # не забыть убрать
tests_path = input("Введите путь к файлу tests.json")

with open(values_path, 'r') as file:
    values_data = json.load(file)
values_df = pd.json_normalize(values_data['values'])
with open(tests_path, 'r') as file:
    tests_data = json.load(file)

id_list = values_df['id'].tolist()
value_list = values_df['value'].tolist()
id_value_pairs = dict(zip(id_list, value_list))

replace_item(tests_data, 'value', id_value_pairs)
print(tests_data)

json_res = json.dumps(tests_data, indent=4)
with open("report.json", "w") as outfile:
    outfile.write(json_res)
