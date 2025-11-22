import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class StrongPasswordValidator:
    """
    Validate whether the password is strong enough:
    - Minimum 8 characters
    - At least 1 uppercase
    - At least 1 number
    - At least 1 special character
    """
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(_("Password must be at least 8 characters long."))
        if not re.search(r"[A-Z]", password):
            raise ValidationError(_("Password must contain at least one uppercase letter."))
        if not re.search(r"\d", password):
            raise ValidationError(_("Password must contain at least one number."))
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError(_("Password must contain at least one special character."))

    def get_help_text(self):
        return _(
            "Your password must contain at least 8 characters, "
            "1 uppercase letter, 1 number, and 1 special character."
        )
