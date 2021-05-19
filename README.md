# Authorization in Flask
We're going to build the same super basic user authentication app as before, but this time with Flask as our backend instead of Express!

### Overview
A react frontend is already provided in the `frontend` folder. Take a little tour of it, and re-familiarize yourself with the auth flow.

A flask backend skeleton is already set up. It contains a create-users migration that is ready to run, and a user model. The `application.py` is also ready to start building routes.

### Setup
To set up the front end:
1. `cd` into the folder
1. Create a `.env` file and put your `REACT_APP_BACKEND_URL` into it.
1. `yarn install`
1. `yarn start`

To set up the back end:
1. `cd` into the folder
1. Create a `.env` file and put your `DATABASE_URL` into it.
1. Set up a virtual environment & activate it
1. `pip3 install -r requirements.txt`
1. Create a database (name corresponding to your DATABASE_URL), and run migrations
1. `python3 application.py`

### Auth flow
1. A user can create an account: inserts a row into our `users` table, and sends the user json (including email and id). If there is an error (for example, email already taken), send a meaningful error message back to the frontend. The http route for this will be `POST /users`.
1. A user can login: look up the user with the email submitted in the request, and check if that user's password is the same as the password submitted in the request. If they match, send back the user json. If not, send an error message. The http route for this will be `POST /users/login`.
1. A user can log out: this is handled entirely by the frontend. It clears the userId from localStorage, and sets the user state to an empty object.
1. When the frontend gets loaded, it will make a call to the `GET /users/verify` endpoint. This call will include a user id in its Authorization header. Look up the user with that id. If there is one, respond with the user json. If not, send an error message.

### Notes
While flask does come with some things that we had to install manually in express (body parsing, logging, routes table, etc.), it does NOT come with cors permitting. We have to install it:
```
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```
This package has a known side effect: on the frontend every error will be masked as a CORS error. The real error is still visible in backend though.



