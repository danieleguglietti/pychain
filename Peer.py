from dataclasses import dataclass

from requests import get

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

    def get_blocks(self):
        """Get blocks of the peer
        :return: List of blocks
        """
        response = get(f"http://{self.__address}:8000/blocks")
        return [Block.from_dict(block) for block in response.json()]

    def get_block(self, index: int) -> Block:
        """Get block of the peer
        :param index: index of the block
        :return: Block
        """
        response = get(f"http://{self.__address}:8000/blocks/{index}")
        return Block.from_dict(response.json())
