import json
#python
serialize={
    'name':"Rochak",
    'age':22
}
json_loader=json.dumps(serialize) #converting to json
print (f'Json Object: {json_loader}')

deserialize= json.loads(json_loader)
print(f'Python-Dict: {deserialize}')