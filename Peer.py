from typing import List

from Block import Block


class Peer(object):
    def get_blocks(self) -> List[Block]:
        """Get blocks of the peer
        :return: List of blocks
        """
        ...
