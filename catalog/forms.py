import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    """
    Form for a librarian to renew a loaned book.
    """
    renewal_date = forms.DateField(
        help_text="Enter a date between now and 4 weeks (default 3).",
    )
    def clean_renewal_date(self):
        # 'cleaned_data' sanitizes the data from the user input.
          # We will work with that sanitized data and then return either
          # the data or raise 'ValidationError'.
        data = self.cleaned_data['renewal_date']

        # Check if a date is in the past.
        if data < datetime.date.today():
            raise ValidationError(
                _('Invalid date - renewal in past')
            )

        # Check if a date is in the allowed range, from now to 4 weeks
        # in future.
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead')
            )

        # Return the `data` that has been processed (cleaned).
        return data