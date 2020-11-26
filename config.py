import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # This allows the application to customize the configuration.
    # Add appropriate code if want to implement some app level customization
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = False
    DB1 = 'chinook.sqlite'
    DB2 = 'jfs1.sqlite'
    DB3 = 'jfs2.sqlite'

    # SQLALCHEMY_DATABASE_URI is the default connection used if bind key = None (or no bind key is specified in the model)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, DB1)

    # see http://flask-sqlalchemy.pocoo.org/2.3/binds/
    SQLALCHEMY_BINDS = {
        "db2":"sqlite:///" + os.path.join(basedir, DB2),
        "db3":"sqlite:///" + os.path.join(basedir, DB3)
    }

class ProductionConfig(Config):
    DEBUG = False
    EXPLAIN_TEMPLATE_LOADING = False
    DB1 = 'chinook.sqlite'
    DB2 = 'jfs1.sqlite'
    DB3 = 'jfs2.sqlite'

    # SQLALCHEMY_DATABASE_URI is the default connection used if bind key = None (or no bind key is specified in the model)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, DB1)

    # see http://flask-sqlalchemy.pocoo.org/2.3/binds/
    SQLALCHEMY_BINDS = {
        "db2":"sqlite:///" + os.path.join(basedir, DB2),
        "db3":"sqlite:///" + os.path.join(basedir, DB3)
    }

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

# Set this to config["key"].  It sets the configuration in app/__init__.py
conf = config["development"]
