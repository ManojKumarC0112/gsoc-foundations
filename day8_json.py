import json
student={
     "id":1,
    "name":"manoj",
    "marks":98,
    "passed":True
 }
json_string=json.dumps(student)
print(student)
print(json_string)

data = '{"id":102,"name":"Asha","marks":72}'
di=json.loads(data)
print(di)
for key,value in di.items():
    print(f'{key}: {value}')
