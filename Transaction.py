"""Defines Transaction class
TODO: properties
TODO: compute_hash
TODO: sign
TODO: check
"""


class Transaction(object):
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
