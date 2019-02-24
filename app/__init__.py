from flask import Flask

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

UPLOAD_FOLDER = './uploads'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config.from_object(__name__)
filefolder=app.config['UPLOAD_FOLDER']
from app import views

