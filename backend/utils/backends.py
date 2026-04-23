from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

from apps.common.models import BlacklistedToken
from apps.users.models import User as MainUser
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            access_token = self.get_raw_token(request.headers.get("Authorization"))
            raw_token = self.get_raw_token(request.data.get("refresh_token"))
            access_found = BlacklistedToken.objects.filter(
                access_token=access_token
            ).exists()
            print(f"Access found: {access_found}")
            refresh_found = BlacklistedToken.objects.filter(
                refresh_token=raw_token
            ).exists()
            if access_found or refresh_found:
                raise InvalidToken("This token has been blacklisted.")
            return super().authenticate(request)
        except InvalidToken:
            raise InvalidToken("Invalid or blacklisted token")


class CustomBackend(ModelBackend):
    """Custom Backend Model"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        :param request:
        :param username:  (Default value = None)
        :param password:  (Default value = None)
        """
        if username is None:
            return None
        if "@" in username:
            kwargs = {"email": username}
        else:
            kwargs = {"username": username}
        try:
            user = MainUser.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except ObjectDoesNotExist:
            return None
