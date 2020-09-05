from flask import Flask, jsonify, request

app = Flask(__name__)

department = [{'Name': "Electricity",
          'dept_id': "0"},

         {'Name': "Transport",
          'dept_id': "1"},

        {'Name': "Sanitary",
          'dept_id': "2"},

        {'Name': "Water",
          'dept_id': "3"},
        ]
@app.route('/')
def index():
        return "Welcome to the Online Complaints API"

@app.route("/depts", methods=['GET'])
def get():
        return jsonify({'Departments':department})

@app.route("/depts/<int:dept_id>",methods={'GET'})
def get_book(dept_id):
        return jsonify({'Department': department[dept_id]})

@app.route("/depts", methods=['POST'])
def create():
        dept = {'Name': "Education",
                'dept_id': "4"},
        department.append(dept)
        return jsonify({'Created': department})



@app.route("/depts/<int:dept_id>",methods=['DELETE'])
def delete(dept_id):
        department.remove(department[dept_id])
        return jsonify({'result': True})


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000, debug=True)





