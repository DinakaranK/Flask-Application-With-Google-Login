from flask import Flask, url_for,redirect, session,render_template
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'dinakaran1998'
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id="170052710339-jc3r30g31cso6kenoqp8dasvnooagpdn.apps.googleusercontent.com",
    client_secret="w5_yb4k9jWGOqS5joHiShOz4",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')

def hello_world():
    email = dict(session).get('email',None)
    return render_template('Home.html')

@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    # do something with the token and profile
    session['email'] = user_info['email']
    return "Login Using Google is Successful"

