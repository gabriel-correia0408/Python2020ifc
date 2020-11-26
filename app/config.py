# importações
import os

from flask import Flask
from flask_cors import CORS  # permitir back receber json do front
from flask_sqlalchemy import SQLAlchemy

# flask
app = Flask(__name__)
CORS(app)  # aplicar o cross domain
# sqlalchemy com sqlite
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'pessoas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # remover warnings
db = SQLAlchemy(app)
