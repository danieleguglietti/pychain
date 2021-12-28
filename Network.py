from Block import Block
from Peer import Peer


class Network(object):
    def notify(self, block: Block) -> None:
        """Notify all the nodes in the network about the new block
        :param block: the new block
        """
        ...

    def accept(self, peer: Peer) -> None:
        """Accept a new node in the network
        :param peer: the new node
        """
        ...

    def __iter__(self) -> Peer:
        """Iterate over all the nodes in the network
        """
        ...
