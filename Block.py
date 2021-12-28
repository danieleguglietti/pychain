"""Defines block classes and other utility functions for blockchain's blocks.
"""
from dataclasses import dataclass, field
from hashlib import sha256
from time import time
from typing import List

from Transaction import Transaction


@dataclass
class Block(object):
    __index: int
    __timestamp: float
    __data: List[Transaction]
    __previous_hash: str
    __nonce: int = field(init=False, default=0)
    __hash: str = field(init=False)

    def __post_init__(self):
        self.__hash = self.compute_hash()

    def compute_hash(self) -> str:
        """Calculates the hash of the block.
        :return: The calculated hash.
        """
        hash_str = f"{self.__index}x{self.__timestamp}{self.__data}x{self.__nonce}x{self.__previous_hash}"
        return sha256(hash_str.encode()).hexdigest()

    def check(self, other: "Block") -> bool:
        """Check whether the block is valid.
        :param other: The other block.
        :return: True of the block is valid, False otherwise.
        """
        return (
                self.__hash == self.compute_hash()
                and self.__index == other.__index + 1
                and self.__previous_hash == other.__hash
        )

    def mine(self, difficulty: int) -> None:
        """Mine the block.
        :param difficulty: The difficulty level.
        """
        while not self.__hash.startswith("0" * difficulty):
            self.__nonce += 1
            self.__hash = self.compute_hash()


class GenesisBlock(Block):
    def __init__(self) -> None:
        super().__init__(0, time(), [], None)
