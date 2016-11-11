__author__ = 'yoandy'

from paypal import settings


class Currency(object):

    @classmethod
    def convert(cls, amount, from_curr, to_curr):
        new_amount = -1
        try:
            new_amount = amount / settings.CURRENCIES[from_curr][to_curr]
            new_amount += settings.MULTICAJA_FEE

            paypal_fee = new_amount * settings.PAYPAL_FEE / 100
            new_amount += paypal_fee
        except KeyError:
            raise Exception("Conversion from %s to %s is not available")

        return new_amount
