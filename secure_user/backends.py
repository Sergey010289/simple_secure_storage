from django.contrib.auth import login
from django.contrib.auth.models import BaseUserManager, UserManager
from secure_user.models import User

__author__ = 'smuravko'


class EmailAuthBackend(UserManager):
    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
