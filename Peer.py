from dataclasses import dataclass
from typing import List

from Block import Block


@dataclass
class Peer(object):
    __address: str

    @property
    def address(self) -> str:
        """Get address of the peer
        :return: Address
        """
        return self.__address

    def get_blocks(self) -> List[Block]:
        """Get blocks of the peer
        :return: List of blocks
        """
        ...

    def get_block(self, index: int) -> Block:
        """Get block of the peer
        :param index: index of the block
        :return: Block
        """
        ...
