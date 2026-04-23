#!/usr/bin/env python3

from ninja import Schema
from pydantic import EmailStr
from typing import Optional


class RegisterSchoolSchema(Schema):
    school_name: str
    email: EmailStr
    password: str
    address: str


class APIResponseSchema(Schema):
    success: bool
    message: str
    data: Optional[dict] = None


class ErrorResponseSchema(Schema):
    success: bool
    message: str


class MessageSchema(Schema):
    """
    Message Schema
    Params:
        @message: str
        @status: int
    """
    message: str
    status: int


class ErrorSchema(Schema):
    """
    Error Schema
    Params:
        @message: str
        @status: int
    """
    error: str
    status: int
