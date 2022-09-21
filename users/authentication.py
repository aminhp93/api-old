# users/authentication.py

from firebase_admin import auth
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request

from .models import CustomUser

class FireBaseAuth(BaseAuthentication):
    def authenticate(self: "FireBaseAuth", request: Request):
        auth_token = request.META.get('HTTP_AUTHORIZATION')
        # print(13, auth_token)
        if not auth_token:
            return None

        # id_token = auth_token.split(' ').pop()
        id_token = auth_token.replace("Bearer ", "")

        if not id_token:
            return None

        try:
            decoded_token = auth.verify_id_token(id_token)
            print(decoded_token)
        except Exception as e:
            if hasattr(e, 'args') and e.args and len(e.args) > 0:
                if 'Token expired' in e.args[0]:
                    raise exceptions.AuthenticationFailed('Token expired')
            raise exceptions.AuthenticationFailed('Invalid token')

        try:
            firebase_user_id = decoded_token['user_id']
        except KeyError:
            raise exceptions.AuthenticationFailed('The user provided with the auth token is not a valid Firebase user, it has no Firebase UID')

        try:
            user = CustomUser.objects.get(firebase_user_id=firebase_user_id)
            return user, None
        except CustomUser.DoesNotExist:
            return None
