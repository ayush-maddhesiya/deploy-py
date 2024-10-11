from flask import Flask, render_template,jsonify, request
from controller import you_name, you_name2, you_name3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')  


# another route that return some json data to test the API
@app.route('/api', methods=['GET'])
def api():
    data = {
        "name": "Ayush",
        "project": "py-versal",
        "status": "In Progress",
        "tasks": ["Setup Vercel", "Create Flask API", "Deploy Flask app"]
    }
    return jsonify(data)

@app.route('/name', methods=['get'])
def name():
    return you_name()

@app.route('/name2', methods=['get'])
def name2():
    return you_name2()

@app.route('/name3', methods=['get'])
def name3():
    return you_name3()

if __name__ == '__main__':
    app.run(debug=True)