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
