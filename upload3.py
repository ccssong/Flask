from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data = request.files  # data is empty
    return data
    # need posted data here

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port=5000)