"""Defines Transaction class
TODO: sign
"""
from dataclasses import dataclass, field
from hashlib import sha256


@dataclass
class Transaction(object):
    __sender: str
    __recipient: str
    __amount: float
    __hash: str = field(init=False, default="")

    @staticmethod
    def from_dict(transaction: dict) -> 'Transaction':
        """Creates a transaction from a dictionary.
        :param transaction: The transaction as a dictionary.
        :return: The transaction.
        """
        required = ["sender", "recipient", "amount"]
        if not all(key in transaction for key in required):
            raise ValueError("Transaction is missing required fields.")
        return Transaction(
            transaction["sender"],
            transaction["recipient"],
            transaction["amount"]
        )

    def __post_init__(self):
        self.__hash = self.compute_hash()

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
                self.__hash == self.compute_hash()
                and self.__sender != self.__recipient
                and self.__amount > 0
        )

    def as_dict(self) -> dict:
        """Returns the transaction as a dictionary.
        :return: The transaction as a dictionary.
        """
        return {
            'hash': self.__hash,
            'sender': self.__sender,
            'recipient': self.__recipient,
            'amount': self.__amount
        }

    def __repr__(self) -> str:
        return str(self.as_dict())
