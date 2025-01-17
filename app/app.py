from flask import Flask, render_template, request, redirect, url_for
from ModelMgr import ModelMgr

app = Flask(__name__)
model_mgr = ModelMgr()

@app.route('/')
def index():
    local_models = model_mgr.get_local_models()
    downloadable_models = model_mgr.get_downloadable_models() or []
    return render_template('index.html', local_models=local_models, downloadable_models=downloadable_models)

@app.route('/download', methods=['POST'])
def download_model():
    model_name = request.form['model_name']
    model_mgr.download_model(model_name)
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove_model():
    model_name = request.form['model_name']
    model_mgr.remove_local_model(model_name)
    return redirect(url_for('index'))

@app.route('/details/<model_name>')
def model_details(model_name):
    details = model_mgr.show_model_details(model_name)
    return render_template('details.html', model_name=model_name, details=details)

if __name__ == '__main__':
    app.run(debug=True)