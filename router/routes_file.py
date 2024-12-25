import os
from flask import Blueprint, request, jsonify, current_app

bp_file = Blueprint('file_upload', __name__)

@bp_file.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return jsonify({'message': 'File uploaded successfully'}), 200
