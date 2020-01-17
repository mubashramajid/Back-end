from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import EmailType
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
import enum



class EmployeeTypes(enum.Enum):
    LINE_MANAGER = 0
    PROJECT_MANAGER = 1
    EMPLOYEE = 2


class Employee(db.Model):
    __tablename__ = "employee"
    __table_args__ = {

    }
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    #  Employee (Child) table is Foriegn key for Department Table - one to one

    department_id = db.Column(
        db.Integer,
        db.ForeignKey('department.id'),
        nullable=False
    )
    #
    # department = db.relationship("Department", back_populates="employee")

    # #Employee (Parent) table is Primary key for Team Table - one to many RS
    # team = db.relationship("Team", back_populates="Employee")

    # # Employee (Parent) table is primary key for Form table - one to many RS
    # form = db.relationship("Form", back_populates="Employee")



    firstName = db.Column(
        db.Unicode(80),
        nullable=False
    )
    lastName = db.Column(
        db.Unicode(80),
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
    designation = db.Column(
        db.Unicode(80),
        nullable=False
    )
    cnic = db.Column(
        db.String(13),
        unique=True,
        nullable=False
    )
    phonenumber = db.Column(
        db.String(15),
        unique=True,
        nullable=False
    )
    joinDate = db.Column(
        db.String(15),
        # nullable=True
    )
    leaveDate = db.Column(
        db.String(15),
        # nullable=True
    )
    employee_type = db.Column(
        Enum(EmployeeTypes),
        default=EmployeeTypes.EMPLOYEE
    )

    # super_admin = db.Column(
    #     db.Boolean,
    #     default=False
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
