import json
def get_student(student_id):
    if student_id==101:
        return {
            'id':101,
            'name':'Manoj',
            'marks':22
        }
    else:
        return {
            'error':'Student not found'
        }
print(get_student(101))
print(get_student(105))

print(json.dumps(get_student(101)))
print(json.dumps(get_student(105)))