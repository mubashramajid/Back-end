from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import EmailType
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
import enum
from sqlalchemy import Enum
from api.utils.auth import jwt, auth
from api.database.config import db
from flask import g, logging
from sqlalchemy import Enum
from passlib.handlers.md5_crypt import md5_crypt

from sqlalchemy.exc import IntegrityError


class Login(db.Model):
    __tablename__ = "Login"
    __table_args__ = {



    }


    email = db.Column(db.String(length=80),
                          unique=True,
                          nullable=False)

    password = db.Column(db.String(length=80),
                            nullable=False)

    employee_type = db.Column(db.String, Enum('admin','hr' ,'manager', 'employee', name='employee_type'),
                             default='user')

    def __init__(self, password=None, email=None, employee_type='employee', md5_crypt=None):
        self.password = md5_crypt.encrypt(password)
        self.email = email
        self.employee_type = employee_type

    def as_dict(self):
        return {'id': self.id, 'username': self.username, 'email': self.email,
                'employee_type': self.employee_type}

        # Generates auth token.
        def generate_auth_token(self, permission_level):
            if permission_level == 3:

                # Generate admin token with flag 1.
                token = jwt.dumps({'email': self.email, 'admin':3})

                # Return admin flag.
                return token

                # Check if admin.
            elif permission_level == 2:

                # Generate admin token with flag 1.
                token = jwt.dumps({'email': self.email, 'admin': 2})

                # Return admin flag.
                return token
            elif permission_level == 1:

                # Generate admin token with flag 1.
                token = jwt.dumps({'email': self.email, 'admin': 1})

                # Return admin flag.
                return token


                # Return normal user flag.
            return jwt.dumps({'email': self.email, 'admin': 0})

# Generates a new access token from refresh token.
    @staticmethod
    @auth.verify_token
    def verify_auth_token(token):

        # Create a global none user.
        g.user = None

        try:
            # Load token.
            data = jwt.loads(token)

        except Exception as e:
            # If any error return false.
            logging.warning('Not verified. {}'.format(e))
            return False

        # Check if email and admin permission variables are in jwt.
        if 'email' in data and 'admin' in data:

            # Set email from jwt.
            g.user = data['email']

            # Set admin permission from jwt.
            g.admin = data['admin']

            # Return true.
            return True

        # If does not verified, return false.
        return False

    @staticmethod
    def generate_password_hash(password):
# Generate password hash.
        h = md5_crypt.encrypt(password)

        # Return hash.
        return h

    def verify_password_hash(self, password):

        # Return result of verifying password, true or false.
        return md5_crypt.verify(password, self.password)

    def __repr__(self):
    # This is only for representation how you want to see user information after query.
        #return "<User(password='%s', email='%s')>" % (
                      #self.password, self.email, self.created)







