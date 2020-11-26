"""
    JupyterLab_Flask_SQLAlchemy

    venv : Python 3.9
"""

__version__ = "0.1"

import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(run_config):
    print(f"PAB> Python version {sys.version}")
    print(f"PAB> Run configuration = {run_config}")
    conf = config[run_config]

    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(conf)
    db.init_app(app)
    return app
