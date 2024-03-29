"""Defines BlockChain class.
TODO: getbalance
TODO: gettransactions
"""
from dataclasses import dataclass, field
from time import time
from typing import List, Optional

from Block import Block, GenesisBlock
from Network import Network
from Transaction import Transaction


@dataclass
class BlockChain(object):
    __difficulty: int = field(init=False, default=6)
    __blocks: List[Block] = field(init=False)
    __transactions: List[Transaction] = field(init=False)
    __network: Network = field(init=False, default=Network())

    def __init__(self):
        self.__blocks = [GenesisBlock([Transaction("0", "0", 0)])]
        self.__transactions = []

    @property
    def blocks(self) -> List[Block]:
        """Return the list of blocks.
        :return: The list of blocks.
        """
        return self.__blocks

    @property
    def transactions(self) -> List[Transaction]:
        """Return the list of transactions.
        :return: The list of transactions.
        """
        return self.__transactions

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

    @property
    def network(self) -> Network:
        """Return the network.
        :return: The network.
        """
        return self.__network

    def add_transaction(self, sender: str, recipient: str, amount: float) -> Transaction:
        """Add a transaction to the blockchain.
        :param sender: The sender of the transaction.
        :param recipient: The recipient of the transaction.
        :param amount: The amount of the transaction.
        """
        transaction = Transaction(sender, recipient, amount)
        self.__transactions.append(transaction)
        return transaction

    def create_block(self) -> Block:
        """ Create a new block and add it to the chain.
        :return: The new block.
        """
        block = Block(
            __index=len(self.__blocks),
            __timestamp=time(),
            __data=self.__transactions,
            __previous_hash=self.last.hash
        )
        block.mine(self.__difficulty)
        self.__blocks.append(block)
        self.__transactions = []
        return block

    def check(self, chain: Optional[List[Block]]) -> bool:
        """Check the integrity of the chain provided if any, otherwise the chain of the calling instance.
        :param chain: The chain to check.
        :return: True if the chain is valid, False otherwise.
        """
        __blocks = chain if chain is not None else self.__blocks

        for i in range(1, len(__blocks)):
            prev, curr = __blocks[i - 1], __blocks[i]
            if not curr.check(prev):
                return False
        return True

    def resolve(self) -> bool:
        """Resolve conflicts by replacing the chain with the longest one.
        :return: True if the chain was replaced, False otherwise.
        """
        max_chain = None
        max_length = len(self.__blocks)

        for node in self.__network:
            chain = node.get_blocks()
            if len(chain) > max_length and self.check(chain):
                max_chain, max_length = chain, len(chain)

        if max_chain is not None:
            self.__blocks = max_chain
            return True

        return False

    def getbalance(self, address: str) -> float:
        """Return the balance of an address.
        :param address: The address to check.
        :return: The balance of the address.
        """
        balance = 0
        for block in self.__blocks:
            for transaction in block.data:
                if transaction.sender == address:
                    balance -= transaction.amount
                if transaction.recipient == address:
                    balance += transaction.amount

        return balance

    def gettransactions(self, address: str) -> List[Transaction]:
        """Return a list of transactions of an address.
        :param address: The address to check.
        :return: The list of transactions of the address.
        """
        transactions = []
        for block in self.__blocks:
            transactions.extend([transaction for transaction in block.data if
                                 transaction.sender == address or transaction.recipient == address])
        transactions.extend([transaction for transaction in self.__transactions if
                             transaction.sender == address or transaction.recipient == address])
        return transactions
