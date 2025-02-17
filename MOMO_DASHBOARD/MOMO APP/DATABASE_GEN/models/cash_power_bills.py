#!/usr/bin/python3
from models.payments_base import PaymentBase
from models import Base


class CashPowerPayments(Base, PaymentBase):

    __tablename__ = "cash_power_payments"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    