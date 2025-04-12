from flask import Flask

app = Flask(__name__)

from app import main  # importa rutas después de crear la app
