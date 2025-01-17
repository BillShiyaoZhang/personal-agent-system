from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from ModelMgr import ModelMgr

model_mgr_view = Blueprint('model_mgr_view', __name__)
model_mgr = ModelMgr()

@model_mgr_view.route('/models', methods=['GET'])
def index():
    downloaded = request.args.get('downloaded')
    removed = request.args.get('removed')

    local_models = model_mgr.local_models
    downloadable_models = model_mgr.get_downloadable_models()

    return render_template(
        'models.html',
        local_models=local_models,
        downloadable_models=downloadable_models,
        downloaded=downloaded,
        removed=removed
    )


@model_mgr_view.route('/models', methods=['POST'])
def download_model():
    model_name = request.form.get('model_name')
    if not model_name:
        data = request.json
        model_name = data.get('model')
    success = model_mgr.download_model(model_name)
    if not success:
        return jsonify({"error": f"Some error. Model {model_name} is not downloaded."}), 400
    return redirect(url_for('model_mgr_view.index', downloaded=model_name))


@model_mgr_view.route('/models/<model_name>', methods=['DELETE'])
def remove_model(model_name):
    success = model_mgr.remove_local_model(model_name)
    if not success:
        return jsonify({"error": f"Some error. Model {model_name} is not removed."}), 400
    return redirect(url_for('model_mgr_view.index', removed=model_name))


@model_mgr_view.route('/models/<model_name>', methods=['GET'])
def show_model_details(model_name):
    details = model_mgr.show_model_details(model_name)
    return render_template('model_details.html', model_name = model_name,details=details)
