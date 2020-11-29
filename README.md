# jupyterlab_flask_sqlalchemy

Provide a standard pattern to use a Flask app, Flask app models, and Flask-sqlalchemy db object in a JupyterLab notebook.

This allows you to develop, troubleshoot and test database model classes/objects in a JupyterLab notebook prior to deploying to the full Flask web application.

Note that this pattern does not include all of the *.py files (controllers, views, etc) required to run as a Flask web application. It includes the minimum set of files--models, config, \_\_init\_\_--necessary to use the Flask app and SQLAlchemy derived classes in a JupyterLab notebook.

## Platform

Python 3.9, Flask, Flask-sqlalchemy, SQLAlchemy, sqlite3

## Files
* config.py : SQLAlchemy configuration settings
* \_\_init\_\_.py : Flask create_app() application factory
* models_chinook.py, models_db2.py, models_db3.py : database models
    - These classes represent three very simple databases.
* chinook.sqlite, jfs1.sqlite, jfs2.sqlite : sqlite3 database files
    - Small and arbitrary example databases used to demonstrate connecting to multiple databases
* jupyterlab_flask_sqlalchemy.ipynb : JupyterLab notebook that uses SQLAlchemy to access the databases via the Flask app and models

## Quick Start

1. Set app_path and app_directory in JupyterLab notebook.
1. Run notebook
