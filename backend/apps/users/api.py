#!/usr/bin/env python3

from ninja import Router

from .schemas import (
    RegisterSchoolSchema,
    APIResponseSchema,
    ErrorResponseSchema,
)
from .services import create_school_and_admin

router = Router(tags=["Auth"])


@router.post(
    "/register-school",
    response={
        201: APIResponseSchema,
        400: ErrorResponseSchema,
    },
)
def register_school(request, payload: RegisterSchoolSchema):
    """
    Register a new school and create an admin account.

    Flow:
    - Creates a School
    - Creates an ADMIN user linked to the school

    Returns:
    - 201: On successful creation
    - 400: If validation fails (e.g., email exists)
    """

    try:
        user = create_school_and_admin(payload)

        return 201, {
            "success": True,
            "message": "School registered successfully",
            "data": {
                "email": user.email,
                "role": user.role,
                "school": user.school.name,
            },
        }

    except ValueError as e:
        return 400, {
            "success": False,
            "message": str(e),
        }

    except Exception:
        return 400, {
            "success": False,
            "message": "Something went wrong while creating the school",
        }
