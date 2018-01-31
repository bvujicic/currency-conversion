"""
Business logic services.
"""
import requests
from decimal import Decimal


CONVERSION_ENDPOINT_URL = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR'


def make_eur_to_btc_conversion(*, eur_value):
    """
    Converts EUR to BTC.

    :param eur_value:  (decimal) Amount of EUR
    :return: conversion: (tuple) Amount of BTC, BTC - EUR exchange rate
    """
    response = requests.get(url=CONVERSION_ENDPOINT_URL)

    response_dict = response.json()
    btc_price = response_dict.get('EUR', None)

    if btc_price is None:
        return

    btc_price = Decimal(btc_price)
    btc_value = eur_value / btc_price

    return btc_value, btc_price
