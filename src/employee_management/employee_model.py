from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import EmailType
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
import enum


class EmployeeTypes(enum.Enum):
    LINE_MANAGER = 0
    PROJECT_MANAGER = 1
    EMPLOYEE = 2


class Employee(db.Model):
    __tablename__ = "Employee"
    __table_args__ = {

    }
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    firstName = db.Column(
        db.Unicode(80),
        unique=True,
        nullable=False
    )
    lastName = db.Column(
        db.Unicode(80),
        unique=True,
        nullable=False
    )
    email = db.Column(
        EmailType,
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(128),
        nullable=False
    )
    gender = db.Column(
        db.Boolean,
        nullable=False
    )

    # super_admin = db.Column(
    #     db.Boolean,
    #     default=False
    # )

    cnic = db.Column(
        db.String(13),
        unique=True,
        nullable=False
    )

    # phonenumber = db.Column(
    #     db.String(15),
    #     unique=True,
    #     nullable=False
    # )

    # profile = relationship(
    #     "Profile",
    #     uselist=False,
    #     back_populates="user"
    # )

    # companies = association_proxy('company_users', 'company')
    #
    # owned_companies = association_proxy("company_users", "owned_company")

    def __repr__(self):
        return '<User %r>' % self.email

    def __str__(self):
        return self.email

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def password_hash(self):
        raise AttributeError('`password` is not a readable attribute')

    @password_hash.setter
    def password_hash(self, password):
        self.password = generate_password_hash(password)


