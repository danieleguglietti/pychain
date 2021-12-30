from dataclasses import dataclass, field
from typing import List, Iterator

from requests import get

from Block import Block
from Peer import Peer


@dataclass
class Network(object):
    __nodes: List[Peer] = field(init=False, default_factory=list)

    def notify(self, block: Block) -> None:
        """Notify all the nodes in the network about the new block
        :param block: the new block
        """
        for node in self.__nodes:
            get(f"http://{node.address}/resolve")

    def accept(self, peer: Peer) -> None:
        """Accept a new node in the network
        :param peer: the new node
        """
        self.__nodes.append(peer)

    def __iter__(self) -> Iterator[Peer]:
        """Iterate over all the nodes in the network
        """
        return iter(self.__nodes)
