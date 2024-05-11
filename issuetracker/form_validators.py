from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class StatusValidator(BaseValidator):
    message = 'Status name must contain only letter'
    code = 'status_validator_error'

    def compare(self, a, b):
        for char in a:
            if char in b:
                return True

        return False


def validate_language(string):
    if not string.isascii():
        raise ValidationError('This field must be in English')


def check_len(string):
    if len(string.split()) == 1:
        raise ValidationError('Must contain at least two words')
