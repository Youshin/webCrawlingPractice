import json

json_str = '{"name": "kim", "age":"32"}'
json_obj = json.loads(json_str)

print(json_obj)
print(type(json_obj))
print(json_obj['age'])