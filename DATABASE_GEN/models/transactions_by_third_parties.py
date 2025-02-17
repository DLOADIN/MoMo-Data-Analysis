#!/usr/bin/python3

from models.payments_base import PaymentBase
from models import Base


class PaymentToThirdParty(Base, PaymentBase):

    __tablename__ = "payments_to_third_parties"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
