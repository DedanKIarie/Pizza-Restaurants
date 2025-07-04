import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DB_URI", f"sqlite:///{os.path.join(basedir, '..', 'instance', 'app.db')}"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JSONIFY_PRETTYPRINT_REGULAR = True
