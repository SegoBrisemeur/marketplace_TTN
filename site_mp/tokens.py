from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, thing, timestamp):
        return (
            six.text_type(thing.pk) + six.text_type(timestamp) +
            six.text_type(thing.is_active)
        )
link_token = TokenGenerator()
