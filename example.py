from flask import Flask, render_template, redirect, jsonify, request
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("upload3.html", name = 'eunsong', language='fucking python')

"""
languages = [{'name' : 'javascript'}, {'name' : 'python'}, {'name' : 'ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

@app.route('/lang2', methods=['POST'])
def addOne():
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'languages' : languages})"""

if __name__ =='__main__':
    app.run(debug=True)