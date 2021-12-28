"""Defines Transaction class
TODO: compute_hash
TODO: sign
TODO: check
"""
from dataclasses import dataclass


@dataclass
class Transaction(object):
    __sender: str
    __recipient: str
    __amount: float

    @property
    def sender(self) -> str:
        """Returns the sender of the transaction.
        :return: The sender of the transaction.
        """
        return self.__sender

    @property
    def recipient(self) -> str:
        """Returns the recipient of the transaction.
        :return: The recipient of the transaction.
        """
        return self.__recipient

    @property
    def amount(self) -> float:
        """Returns the amount of the transaction.
        :return: The amount of the transaction.
        """
        return self.__amount

    def compute_hash(self) -> str:
        """Calculates the hash of the transaction.
        :return: The calculated hash.
        """
        ...

    def sign(self, private_key: str) -> None:
        """Signs the transaction with the given private key.
        :param private_key: The private key to sign with.
        """
        ...

    def check(self) -> bool:
        """Checks whether the transaction is valid.
        :return: True if the transaction is valid, False otherwise.
        """
        ...
