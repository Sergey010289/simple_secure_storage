from django.db import models

__author__ = 'smuravko'


class CustomDocumentManager(models.Manager):
    def create(self, private_number=None, summary=None, **extra_fields):
        document = self.model(_private_number=private_number,
                              _summary=summary,
                              **extra_fields)
        document.save()
        return document
