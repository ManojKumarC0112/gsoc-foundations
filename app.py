from flask import *
import json

app=Flask(__name__)

@app.route('/students/<int:student_id>')
def getstudents(student_id):
    if student_id==101:
        return jsonify({
            'id':101,
            'name':'manoj',
             'marks':99
        })
    else:
        return jsonify(
            {
                'error':'Student not found'
            }
        ),404

if __name__=='__main__':
    app.run(debug=True)
else:
    app.run(debug=False)