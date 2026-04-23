from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import School

User = get_user_model()

def create_school_and_admin(data):
    """
    Creates a school and assigns the registering user as ADMIN.

    Raises:
        ValueError: If email already exists
    """

    if User.objects.filter(email=data.email).exists():
        raise ValueError("User with this email already exists")

    school = School.objects.create(name=data.school_name)

    user = User.objects.create(
        email=data.email,
        role="ADMIN",
        school=school,
    )
    user.set_password(data.password)
    user.save()

    return user


def generate_tokens(user):
    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None

    if not user.check_password(password):
        return None

    return user