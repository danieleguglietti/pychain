from dataclasses import dataclass, field
from typing import Set, Iterator

from requests import get

from Peer import Peer


@dataclass
class Network(object):
    __nodes: Set[Peer] = field(init=False, default_factory=set)

    @property
    def nodes(self) -> Set[Peer]:
        """Get the nodes in the network
        """
        return self.__nodes

    def notify(self) -> None:
        """Notify all the nodes in the network about the new block
        """
        for node in self.__nodes:
            get(f"http://{node.address}/resolve")

    def accept(self, peer: Peer) -> None:
        """Accept a new node in the network
        :param peer: the new node
        """
        self.__nodes.add(peer)

    def __iter__(self) -> Iterator[Peer]:
        """Iterate over all the nodes in the network
        """
        return iter(self.__nodes)
