"""
Conversion models.

DOC: Log each conversion request in the database (date-time, conversion-rate, EUR amount, request IP).
"""

from django.db import models

from web.abstract import TimestampModel


class Conversion(TimestampModel):
    """
    Conversion info model.
    """
    eur_amount = models.DecimalField(verbose_name='euro amount', max_digits=10, decimal_places=2)
    conversion_rate = models.DecimalField(verbose_name='conversion_rate', max_digits=10, decimal_places=2)
    request_ip = models.GenericIPAddressField(verbose_name='request IP')

    class Meta:
        db_table = 'euro_coversion'

    def __str__(self):
        return '{} {}'.format(self.conversion_rate, self.request_ip)
