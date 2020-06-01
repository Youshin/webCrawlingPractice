import json

with open('json_example.json','r', encoding='utf8') as f:
    content = f.read()
    json_obj = json.loads(content)
    print(json_obj)
    print('\n',json_obj['employees'],'\n')
    for dd in json_obj['employees']:
        print(dd['firstName'],dd['lastName'])