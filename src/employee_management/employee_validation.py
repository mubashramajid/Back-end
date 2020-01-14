from marshmallow import Schema, fields, validates_schema, ValidationError, validate
from marshmallow_enum import EnumField
# from password_strength import PasswordPolicy
import re
import phonenumbers
from src.employee_management import EmployeeTypes


class EmployeeValidation(Schema):
    """
    This is the validation schema for user registration.
    """
    first_name = fields.String(
        required=True,
        error_messages={"required": "Please enter first name."}
    )

    last_name = fields.String(
        required=True,
        error_messages={"required": "Please enter last name."}
    )

    cnic = fields.String(
        required=True,
        error_messages={"required": "Please enter CNIC number."},
        validate=validate.Length(min=13, max=13)
    )

    gender = fields.Boolean(
        required=True,
        error_messages={"required": "Please specify the Gender."}
    )

    email = fields.Email(
        required=True,
        error_messages={"required": "Please enter Email."}
    )

    phonenumber = fields.String(
        required=True,
        error_messages={"required": "Please enter Contact Number."}
    )

    employee_type = EnumField(
        EmployeeTypes,
        required=True,
        error_messages={"required": "Please select Employee Type."}
    )
    #10/1/2020

    designation = fields.String(
        required=True,
        error_messages={"required": "Please enter designation."}
    )
    join_Date = fields.Date(
        required=True,
        error_messages={"required": "Please enter joining date."}
    )
    leave_Date = fields.Date(
        required=True,
        error_messages={"required": "Please enter leaving date."}
    )

    # we are explicitly keeping load_only True, to avoid any accident where we write the password to JSON.
    # If anyone mistakenly re-used this schema for Response, it will never send password in the JSON.
    password = fields.String(
        load_only=True,
        required=True,
        error_messages={"required": "Please set a password for your account."}
    )

    confirm_password = fields.String(
        load_only=True,
        required=True,
        error_messages={"required": "Please provide a confirm password."}
    )

    @validates_schema
    def validate_password(self, data, **kwargs):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError(
                field_name="confirm_password",
                message="The Confirm Password does not match with the Password."
            )

    @validates_schema
    def validate_phonenumber(self, data, **kwargs):
        phonenumber = data.get("phonenumber")

        try:
            if not phonenumbers.is_valid_number(phonenumbers.parse(phonenumber)):
                raise ValidationError(
                    field_name="phonenumber",
                    message="Invalid Phone number format. "
                )
        except:
            raise ValidationError(
                field_name="phonenumber",
                message="Invalid Phone number format. "
            )


class EmployeeValidationUpdate(Schema):
    """
    This is the validation schema for user registration.
    """
    first_name = fields.String(
        required=True,
        error_messages={"required": "Please enter first name."}
    )

    last_name = fields.String(
        required=True,
        error_messages={"required": "Please enter last name."}
    )

    cnic = fields.String(
        required=True,
        error_messages={"required": "Please enter CNIC number."},
        validate=validate.Length(min=13, max=13)
    )

    gender = fields.Boolean(
        required=True,
        error_messages={"required": "Please specify the Gender."}
    )

    email = fields.Email(
        required=True,
        error_messages={"required": "Please enter Email."}
    )

    phonenumber = fields.String(
        required=True,
        error_messages={"required": "Please enter Contact Number."}
    )

    employee_type = EnumField(
        EmployeeTypes,
        required=True,
        error_messages={"required": "Please select Employee Type."}
    )
    @validates_schema
    def validate_phonenumber(self, data, **kwargs):
            phonenumber = data.get("phonenumber")

            try:
             if not phonenumbers.is_valid_number(phonenumbers.parse(phonenumber)):
                raise ValidationError(
                    field_name="phonenumber",
                    message="Invalid Phone number format. "
                )
            except:
                raise ValidationError(
                    field_name="phonenumber",
                    message="Invalid Phone number format. "
            )