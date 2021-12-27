"""Defines block classes and other utility functions for blockchain's blocks.
TODO: properties
TODO: compute_hash
TODO: check
TODO: __eq__
TODO: mine
TODO: isnext
"""
from dataclasses import dataclass


@dataclass
class Block(object):
    def compute_hash(self) -> str:
        """Calculates the hash of the block.
        :return: The calculated hash.
        """
        ...

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
