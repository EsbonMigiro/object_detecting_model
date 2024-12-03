from flask import Flask, jsonify, request
import os
import sys
from flask_cors import CORS 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utilities.dir_creator import ProjectDirectoryManager
from utilities.detect import detect


app = Flask(__name__)
CORS(app)  # This will allow all domains to access your API

UPLOAD_FOLDER = os.path.join(ProjectDirectoryManager.paths['IMAGE_PATH'], 'input')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/api', methods=['GET'])
def api_home():
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route('/api/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file to ./images/input
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    #detect
    detect(file.filename)


    return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200



if __name__ == '__main__':
    host = '0.0.0.0' 
    port = 5000  
    print(f"Server running on http://{host}:{port}")
    app.run(debug=True, host=host, port=port)

