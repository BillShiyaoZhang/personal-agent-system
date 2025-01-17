from flask import Flask, render_template, url_for
from ModelMgr import ModelMgr
from ModelMgrView import model_mgr_view

app = Flask(__name__)
model_mgr = ModelMgr()

@app.route('/')
def index():
    return render_template('index.html', model_mgr_url=url_for('model_mgr_view.index'))

app.register_blueprint(model_mgr_view)

if __name__ == '__main__':
    app.run(debug=True)