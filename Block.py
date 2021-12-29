"""Defines block classes and other utility functions for blockchain's blocks.
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
    __nonce: int = field(default=0)
    __hash: str = field(init=False, default="")

    @staticmethod
    def from_dict(block: dict) -> "Block":
        """Create a block from a dictionary.
        :param block: The dictionary representation of the block.
        :return: The block.
        """
        required = ["index", "timestamp", "data", "previous_hash", "nonce"]
        if not all(key in block for key in required):
            raise ValueError("Invalid block.")
        data = [Transaction.from_dict(tx) for tx in block["data"]]
        return Block(
            block["index"],
            block["timestamp"],
            data,
            block["previous_hash"],
            block["nonce"]
        )

    def __post_init__(self):
        self.__hash = self.compute_hash()

    @property
    def index(self) -> int:
        """Get the index of the block.
        :return: The index of the block.
        """
        return self.__index

    @property
    def hash(self) -> str:
        """Get the hash of the block.
        :return: The hash of the block.
        """
        return self.__hash

    @property
    def data(self) -> List[Transaction]:
        """Get the data of the block.
        :return: The data of the block.
        """
        return self.__data

    @property
    def timestamp(self) -> float:
        """Get the timestamp of the block.
        :return: The timestamp of the block.
        """
        return self.__timestamp

    @property
    def previous_hash(self) -> str:
        """Get the previous hash of the block.
        :return: The previous hash of the block.
        """
        return self.__previous_hash

    def compute_hash(self) -> str:
        """Calculates the hash of the block.
        :return: The calculated hash.
        """
        return sha256(str(self).encode()).hexdigest()

    def check(self, other: "Block") -> bool:
        """Check whether the block is valid.
        :param other: The other block.
        :return: True of the block is valid, False otherwise.
        """
        return (
                self.__hash == self.compute_hash()
                and self.__index == other.index + 1
                and self.__previous_hash == other.hash
        )

    def mine(self, difficulty: int) -> None:
        """Mine the block.
        :param difficulty: The difficulty level.
        """
        while not self.__hash.startswith("0" * difficulty):
            self.__nonce += 1
            self.__hash = self.compute_hash()

    def as_dict(self) -> dict:
        """Convert the block to a dictionary.
        :return: The dictionary representation of the block.
        """
        return {
            "hash": self.__hash,
            "index": self.__index,
            "timestamp": self.__timestamp,
            "data": self.__data,
            "previous_hash": self.__previous_hash,
            "nonce": self.__nonce
        }

    def __repr__(self) -> str:
        return str(self.as_dict())


class GenesisBlock(Block):
    def __init__(self, data: List[Transaction]) -> None:
        super().__init__(0, 0, data, None)

    def check(self, other: "Block") -> bool:
        return (
                self.index == 0
                and self.hash == self.compute_hash()
                and self.previous_hash is None
                and other.previous_hash == self.hash
        )
