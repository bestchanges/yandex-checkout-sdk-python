# -*- coding: utf-8 -*-
from decimal import Decimal

from yandex_checkout.domain.common.base_object import BaseObject


class Amount(BaseObject):
    """
    Class representing amount data wrapper object
    """
    __value = None

    __currency = None

    @property
    def value(self):
        """
        :return Decimal:
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = Decimal(value)

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = str(value)
