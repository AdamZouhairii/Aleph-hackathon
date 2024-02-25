import os
import subprocess


""" 

python3 -m aleph_client file upload --help


"""

from flask import Flask, request, jsonify
import json 


app = Flask(__name__)

# Add Access-Control-Allow-Origin header to all responses
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    
    file.save(file.filename)
    # execute the command, and get the json output, return it
    command = f"python3 -m aleph_client file upload {file.filename}"
    output = subprocess.getoutput(command)
    
    print(json.loads(output))
    return jsonify(json.loads(output))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
    
