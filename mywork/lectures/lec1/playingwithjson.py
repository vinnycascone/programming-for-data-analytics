import json
data={
'name': 'Joe',
'age' : 21,
"student": True
}

jsonString= json.dumps(data)
print(data)
print(jsonString)