import json

json_data = '{"name": "Ivan", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)
print(parsed_data, type(parsed_data))

print(parsed_data["name"])

data = {"name": "Ivan", "age": 30, "is_student": False}

json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))

with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data, type(read_data))

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4,ensure_ascii=False)
