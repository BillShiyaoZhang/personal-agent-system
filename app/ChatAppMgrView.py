from flask import Blueprint, render_template, request, redirect, url_for, flash
from ChatAppMgr import ChatAppMgr

chat_app_mgr_view = Blueprint('chat_app_mgr_view', __name__)
chat_app_mgr = ChatAppMgr()

@chat_app_mgr_view.route('/chat_apps')
def index():
    installable_apps = chat_app_mgr.list_installable_apps()
    local_apps = chat_app_mgr.list_local_apps()
    return render_template('chat_apps.html', installable_apps=installable_apps, local_apps=local_apps)

@chat_app_mgr_view.route('/install_app', methods=['POST'])
def install_app():
    app_name = request.form.get('app_name')
    # Assuming ChatAppDefinition has a method to find an app by name
    app = next((app for app in chat_app_mgr.installable_apps if app.name == app_name), None)
    if app:
        chat_app_mgr.install_app(app)
        flash(f'{app.name} 已安装')
    else:
        flash(f'{app_name} 未找到')
    return redirect(url_for('chat_app_mgr_view.index'))

@chat_app_mgr_view.route('/connect_app', methods=['POST'])
def connect_app():
    app_name = request.form.get('app_name')
    model_name = request.form.get('model_name')
    app = next((app for app in chat_app_mgr.local_apps if app.name == app_name), None)
    if app:
        chat_app_mgr.connect(app, model_name)
        flash(f'{app.name} 已连接到模型 {model_name}')
    else:
        flash(f'{app_name} 未找到')
    return redirect(url_for('chat_app_mgr_view.index'))

@chat_app_mgr_view.route('/open_app/<app_name>')
def open_app(app_name):
    app = next((app for app in chat_app_mgr.local_apps if app.name == app_name), None)
    if app:
        chat_app_mgr.open_app(app)
        flash(f'{app.name} 已打开')
    else:
        flash(f'{app_name} 未找到')
    return redirect(url_for('chat_app_mgr_view.index'))

@chat_app_mgr_view.route('/uninstall_app/<app_name>')
def uninstall_app(app_name):
    app = next((app for app in chat_app_mgr.local_apps if app.name == app_name), None)
    if app:
        chat_app_mgr.uninstall_app(app)
        flash(f'{app.name} 已卸载')
    else:
        flash(f'{app_name} 未找到')
    return redirect(url_for('chat_app_mgr_view.index'))