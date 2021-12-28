"""Defines BlockChain class.
TODO: add_transaction
TODO: create_block
TODO: check
TODO: resolve
TODO: getbalance
TODO: gettransactions
"""
from dataclasses import dataclass, field
from typing import List

from Block import Block, GenesisBlock
from Transaction import Transaction


@dataclass
class BlockChain(object):
    __blocks: List[Block] = field(init=False, default_factory=list)
    __transactions: List[Transaction] = field(init=False, default_factory=list)

    def __init__(self):
        self.__blocks = [GenesisBlock([Transaction()])]
        self.__transactions = []

    @property
    def blocks(self) -> List[Block]:
        """Return the list of blocks.
        :return: The list of blocks.
        """
        return self.__blocks

    @property
    def genesis(self) -> Block:
        """Return the genesis block.
        :return: The genesis block.
        """
        return self.__blocks[0]

    @property
    def last(self) -> Block:
        """Return the last block.
        :return: The last block.
        """
        return self.__blocks[-1]

    def add_transaction(self, sender: str, recipient: str, amount: float) -> Transaction:
        """Add a transaction to the blockchain.
        :param sender: The sender of the transaction.
        :param recipient: The recipient of the transaction.
        :param amount: The amount of the transaction.
        """
        ...

    def create_block(self) -> Block:
        """ Create a new block and add it to the chain.
        :return: The new block.
        """
        ...

    def check(self) -> bool:
        """Check the integrity of the chain.
        :return: True if the chain is valid, False otherwise.
        """
        ...

    def resolve(self) -> bool:
        """Resolve conflicts by replacing the chain with the longest one.
        :return: True if the chain was replaced, False otherwise.
        """
        ...

    def getbalance(self, address: str) -> float:
        """Return the balance of an address.
        :param address: The address to check.
        :return: The balance of the address.
        """
        ...

    def gettransactions(self, address: str) -> List[Transaction]:
        """Return a list of transactions of an address.
        :param address: The address to check.
        :return: The list of transactions of the address.
        """
        ...
