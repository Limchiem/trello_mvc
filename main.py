from flask import Flask
import os
from init import db, ma, bcrypt, jwt
from controllers.cli_controller import db_commands

def create_app():
    app = Flask(__name__)

    #                                       dbms        driver      user    pw      url     port    db name
    # app.config["SQLALCHEMY_DATABASE_URI"]="postgresql+psycopg2://trello_dev:123456@localhost:5432/trello_mvc_db"

    # app.config["JWT_SECRET_KEY"]="secret"
    
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)

    return app