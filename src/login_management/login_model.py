from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import EmailType
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
import enum
from sqlalchemy import Enum

class Login(db.Model):
    __tablename__ = "Login"
    __table_args__ = {
           
    }
