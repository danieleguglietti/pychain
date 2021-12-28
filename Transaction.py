"""Defines Transaction class
TODO: sign
"""
from dataclasses import dataclass
from hashlib import sha256


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
        hash_str = repr(self)
        return sha256(hash_str.encode()).hexdigest()

    def sign(self, private_key: str) -> None:
        """Signs the transaction with the given private key.
        :param private_key: The private key to sign with.
        """
        ...

    def check(self) -> bool:
        """Checks whether the transaction is valid.
        :return: True if the transaction is valid, False otherwise.
        """
        return (
                self.sender != self.recipient
                and self.amount > 0
        )

    def __repr__(self) -> str:
        return f"{self.sender}:{self.recipient}x{self.amount}"
