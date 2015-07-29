from django.core.exceptions import ValidationError
__author__ = 'smuravko'


def validate_file(fieldfile_obj):   # TODO: check at working
    filesize = fieldfile_obj.file.size
    megabyte_limit = 10.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
