
from flask import Flask, request, render_template, redirect, url_for, send_file, jsonify
import requests
from pymongo import MongoClient
import os
from bson.json_util import dumps
from io import BytesIO

app = Flask(__name__)

TIKA_SERVER_URL = os.getenv("TIKA_SERVER_URL")
MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client["tika_results"]
collection = db["analyses"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    if file:
        files = {'file': (file.filename, file.stream, file.mimetype)}
        
        headers = {
            'Accept': 'application/json'
        }
        response = requests.put(f"{TIKA_SERVER_URL}/rmeta/form", files=files, headers=headers)
        result_json = response.json()[0]

        result = {
            "filename": file.filename,
            "metadata": result_json.get("metadata", {}),
            "content": result_json.get("X-TIKA:content", ""),
        }
        collection.insert_one(result)

        return render_template('results.html', filename=file.filename, content=result["content"], metadata=result["metadata"])
    return redirect(url_for('index'))

@app.route('/history')
def history():
    results = list(collection.find({}, {"_id": 0}))
    return render_template('results.html', history=results)

@app.route('/export')
def export():
    results = list(collection.find({}, {"_id": 0}))
    json_data = dumps(results, indent=2)
    return send_file(BytesIO(json_data.encode('utf-8')), download_name="analises.json", as_attachment=True, mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
