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
        return sha256(str(self).encode()).hexdigest()

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

    def as_dict(self) -> dict:
        """Returns the transaction as a dictionary.
        :return: The transaction as a dictionary.
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }

    def __repr__(self) -> str:
        return str(self.as_dict())
