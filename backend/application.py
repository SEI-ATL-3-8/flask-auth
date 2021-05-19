import os
from flask import Flask, request
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
import sqlalchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
import models
models.db.init_app(app)

def root():
  return 'ok'
app.route('/', methods=["GET"])(root)

def create_user():
  existing_user = models.User.query.filter_by(email=request.json["email"]).first()
  if existing_user:
    return { "message": "Email must be present and unique" }, 400
  
  user = models.User(
    email=request.json["email"],
    password=request.json["password"],
  )
  models.db.session.add(user)
  models.db.session.commit()
  return { "user": user.to_json() }
app.route('/users', methods=["POST"])(create_user)

def login():
  user = models.User.query.filter_by(email=request.json["email"]).first()
  if not user:
    return { "message": "User not found" }, 404
  if user.password == request.json["password"]:
    return { "user": user.to_json() }
  else:
    return { "message": "Password incorrect" }, 401
app.route('/users/login', methods=["POST"])(login)

def verify_user():
  user = models.User.query.filter_by(id=request.headers["Authorization"]).first()
  if not user:
    return { "message": "user not found" }, 404
  return { "user": user.to_json() }
app.route('/users/verify', methods=["GET"])(verify_user)

if __name__ == '__main__':
  port = os.environ.get('PORT') or 5000
  app.run('0.0.0.0', port=port, debug=True)
