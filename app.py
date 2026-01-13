from flask import *
import json

app=Flask(__name__)
students={
    '101':{
        'name':'manoj',
    }
}
@app.route('/')
def home():
    return "dont worry working well"
@app.route("/students/<int:student_id>",methods=['GET'])
def get_students(student_id):
    if student_id not in students:
        return jsonify(
            {
                'error':'Student not found'
            }
        ),404
    else:
        return jsonify(students[student_id])

@app.route("/students",methods=['POST'])
def add_students():
    data=request.get_json()

    if data is None:
        return jsonify({"error":"No data"}),404

    if "id" not in data or "name" not in data or "marks" not in data:
        return jsonify({'error':'missing fileds'}),404

    student_id=data['id']

    if student_id in students:
        return jsonify({'error':'Student already exists'}),400

    students[student_id]={
        'id':student_id,
        "name":data['name'],
        "marks":data['marks']
    }
    return jsonify({"message":"Student added successfully"}),200


if __name__=='__main__':
    app.run(debug=True)
else:
    app.run(debug=False)