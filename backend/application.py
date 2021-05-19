import os
from flask import Flask, request
from flask_cors import CORS
import sqlalchemy
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
import models
models.db.init_app(app)

def root():
  return 'ok'
app.route('/', methods=["GET"])(root)

def signup():
  try:
    user = models.User(
      email=request.json["email"],
      password=request.json["password"]
    )
    models.db.session.add(user)
    models.db.session.commit()
    return { "user": user.to_json() }
  except sqlalchemy.exc.IntegrityError:
    return { "message": "email already taken" }, 400
app.route('/users', methods=["POST"])(signup)

def login():
  user = models.User.query.filter_by(email=request.json["email"]).first()

  if user.password == request.json["password"]:
    return { "user": user.to_json() }
  else:
    return { "message": "login failed" }, 401
app.route('/users/login', methods=["POST"])(login)

def verify():
  user = models.User.query.filter_by(id=request.headers["Authorization"]).first()
  print(request.headers)
  if user:
    return { "user": user.to_json() }
  else:
    return { "message": "user not found" }, 404
app.route('/users/verify', methods=["GET"])(verify)

if __name__ == '__main__':
  port = os.environ.get('PORT') or 5000
  app.run('0.0.0.0', port=port, debug=True)