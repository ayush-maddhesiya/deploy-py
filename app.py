from flask import Flask, render_template,jsonify, request

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

if __name__ == '__main__':
    app.run(debug=True)

