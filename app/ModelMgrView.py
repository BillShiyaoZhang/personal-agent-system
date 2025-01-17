from flask import Flask, request, jsonify, render_template, redirect, url_for
from ModelMgr import ModelMgr

app = Flask(__name__)
model_mgr = ModelMgr()

@app.route('/models', methods=['GET'])
def list_models():
    return jsonify(model_mgr.local_models)

@app.route('/models', methods=['POST'])
def download_model():
    model_name = request.form.get('model_name')
    if not model_name:
        data = request.json
        model_name = data.get('model')
    success = model_mgr.download_model(model_name)
    return redirect(url_for('index', downloaded=model_name if success else None))

@app.route('/models/<model_name>', methods=['DELETE'])
def remove_model(model_name):
    model_mgr.remove_local_model(model_name)
    return jsonify({"status": "removed", "model": model_name})

@app.route('/models/<model_name>', methods=['GET'])
def show_model_details(model_name):
    details = model_mgr.show_model_details(model_name)
    return jsonify(details)

@app.route('/', methods=['GET'])
def index():
    downloaded = request.args.get('downloaded')
    local_models = model_mgr.local_models
    downloadable_models = model_mgr.get_downloadable_models()
    return render_template(
        'index.html',
        local_models=local_models,
        downloadable_models=downloadable_models,
        downloaded=downloaded
    )

if __name__ == "__main__":
    app.run(debug=True)
