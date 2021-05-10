from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def heals_check():
    if request.method == 'POST':
        return request.data
    if request.method == 'GET':
        return str(False)

if __name__ == '__main__':
    app.run(port=4567)