from flask import Flask, request, jsonify, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from flask_cors import CORS
import ast

plt.switch_backend('Agg')
app = Flask(__name__)
CORS(app)

students = [
    {"reg_id": 234, "name": "Alice", "class": "10", "division": "A", "progress": [10, 20, 30, 40, 50]},
    {"reg_id": 5231, "name": "Bob", "class": "10", "division": "B", "progress": [15, 25, 35, 45, 55]},
    {"reg_id": 8892, "name": "Charlie", "class": "11", "division": "A", "progress": [20, 30, 40, 50, 60]}
]

student_list = pd.DataFrame(students)

newfile = student_list.to_dict(orient='records')
print(newfile)
try: 
    student_list = pd.read_csv('students_progress.csv')
    student_list['progress'] = student_list['progress'].apply(ast.literal_eval)
    print(student_list['progress'])
except: 
    print('nope')


@app.route('/api/students', methods=['GET'])
def get_students():

    return jsonify(student_list.to_dict(orient='records'))
@app.route('/api/toppers', methods=['GET'])
def get_toppers():
    top_df = pd.DataFrame(students)
@app.route('/api/students', methods=['POST'])
def add_student():
    new_student = request.json
    list1 = []
    for item in new_student.values(): 
        list1.append(item)
    print(list1)
    student_list.loc[len(student_list['reg_id'])] = list1
    return jsonify(student_list.to_dict(orient='records')), 201
@app.route('/api/update', methods=['POST'])
def updateStudents():
    updatedList = request.json
    global student_list
    student_list = pd.DataFrame(updatedList)
    return jsonify(student_list.to_dict(orient='records')), 201

@app.route('/api/delete_user', methods=['POST'])
def deleteUser():
    user_reg = request.json
    print(user_reg['reg_id'])
    global student_list
    student_list.drop(student_list[student_list['reg_id'] == user_reg['reg_id']].index, inplace=True)
    print(student_list)
    return jsonify(student_list.to_dict(orient='records'))

@app.route('/api/progress', methods=['GET'])
def get_progress():
    plt.clf()
    student_list.to_csv('students_progress.csv', index=False)
    
    for i in range(0,len(student_list['progress']), 1):
        plt.plot(student_list.loc[i,'progress'], label=student_list.loc[i, 'name'])
        print(student_list.loc[i, 'progress'], student_list.loc[i, 'name'])

    plt.xlabel('Days')
    plt.ylabel('Progress')
    plt.title('Course Completion Progress')
    plt.legend()
    exam_labels = ['PA1', 'SA1', 'PA2', 'SA2', 'Models_1', 'Models_2']
    ser = pd.Series(exam_labels, index=(range(0,len(exam_labels))))
    print(ser)
    plt.xticks(ticks = ser.index.tolist(), labels=exam_labels)
    imagename = f'progress{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png'
    
    plt.savefig(imagename)
    print(imagename)
    return send_file(imagename, mimetype='image/png')
    


if __name__ == '__main__':
    app.run(debug=True)