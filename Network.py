from Block import Block


class Network(object):
    def notify(self, block: Block) -> None:
        """Notify all the nodes in the network about the new block
        :param block: the new block
        """
        ...

    def __iter__(self):
        """Iterate over all the nodes in the network
        """
        ...
