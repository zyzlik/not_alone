import re

from django.conf import settings
from django import forms

from allauth.account.adapter import DefaultAccountAdapter


class UsernameAccountAdapter(DefaultAccountAdapter):

    def clean_username(self, username, shallow=False):

        errors = {
            'invalid_characters': 'Only latin letters, digits and /./-/_'
        }

        pattern = settings.USERNAME_PATTERN
        if re.match(pattern, username):
            return username
        else:
            raise forms.ValidationError(errors["invalid_characters"])
