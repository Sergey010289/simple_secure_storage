from django.db import models

__author__ = 'smuravko'


class CustomUserManager(models.Manager):
    def create(self, email, password, first_name=None, last_name=None,
               **extra_fields):
        if not email or not password:
            raise ValueError('Missing required parameter')

        user = self.model(email=email, password=password,
                          _first_name=first_name, _last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
