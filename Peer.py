from typing import List

from Block import Block


class Peer(object):
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
