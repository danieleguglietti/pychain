"""Defines block classes and other utility functions for blockchain's blocks.
TODO: properties
TODO: compute_hash
TODO: check
TODO: __eq__
TODO: mine
TODO: isnext
"""
from dataclasses import dataclass, field
from hashlib import sha256
from typing import List

from Transaction import Transaction


@dataclass
class Block(object):
    __index: int
    __timestamp: float
    __data: List[Transaction]
    __previous_hash: str
    __hash: str = field(init=False)

    def __post_init__(self):
        self.__hash = self.compute_hash()

    def compute_hash(self) -> str:
        """Calculates the hash of the block.
        :return: The calculated hash.
        """
        hash_str = f"{self.__index}-{self.__timestamp}-{self.__data}-{self.__previous_hash}"
        return sha256(hash_str.encode()).hexdigest()

    def check(self) -> bool:
        """Check whether the block is valid.
        :return: True of the block is valid, False otherwise.
        """
        ...

    def __eq__(self, other: "Block") -> bool:
        """Check whether the block is equal to another block.
        :param other: The other block.
        :return: True if the blocks are equal, False otherwise.
        """
        ...

    def mine(self, difficulty: int) -> None:
        """Mine the block.
        :param difficulty: The difficulty level.
        """
        ...

    def isnext(self, other: "Block") -> bool:
        """Check whether the block is a child of another block.
        :param other: The other block.
        :return: True if the block is a child of the other block, False otherwise.
        """
        ...


class GenesisBlock(Block):
    def __init__(self) -> None:
        super().__init__()

    def check(self) -> bool:
        """Check whether the block is valid.
        :return: True of the block is valid, False otherwise.
        """
        ...
