from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
import models  

from api.user import user
from api.client import client
from api.api import api


DEBUG = True
PORT = 8000
login_manager = LoginManager()

app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = 'reljreljrle STRING' 
login_manager.login_view = 'user.login'
login_manager.init_app(app)

@login_manager.user_loader 
def load_user(userid):
    print(userid)
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

CORS(user, origins=['http://localhost:3000'], supports_credentials=True)
CORS(api, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(user)
app.register_blueprint(api)

@app.before_request 

def before_request(): 
    g.db = models.DATABASE
    g.db.connect()


def after_request():
    g.db.close()
    return response


@app.route('/') 

def index():
    return 'hi'
    
if __name__ == '__main__': 
    models.initialize() 
    app.run(debug=DEBUG, port=PORT) 


