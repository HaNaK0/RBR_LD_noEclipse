__author__ = 'HaNaK0'

import constants as con


class Path(object):
    """
    path instances to keep track of paths
    """

    def __init__(self, index, owner):
        """
        Init
        :return:
        """
        self.index = index
        self.nodes = []
        self.pType = owner.OTYPE
        self.owner = owner

    def add(self, node):
        """
        adds a node to the path
        :param node:ig.PathPoint
        :return: index
        """
        if self.pType == con.PMC["WALKING"]:
            # checks if to store new path Node
            if len(self.nodes) == 0:  # if no nodes exist
                self.nodes.append(node)
                return 0
            elif len(self.nodes) == 1:  # if 1 node exist
                if node.posGridX > self.nodes[0].posGridX:  # if new node is right of old node
                    self.nodes.append(node)
                    return 1
                else:  # if node is left of existing node
                    self.nodes.append(self.nodes[0])
                    self.nodes[0] = node
                    return 0
            elif len(self.nodes) == 2:  # if 2 nodes exist
                if node.posGridX < self.nodes[0].posGridX:  # if new node is left of the leftmost Node
                    self.nodes[0] = node
                    return 0
                elif node.posGridX > self.nodes[1].posGridX:  # if new node is right of the rightmost node
                    self.nodes[1] = node
                    return 1

        if self.pType == con.PMC["FLYING"]:
            self.nodes.append(node)
            nodeIndex = len(self.nodes) - 1
            return nodeIndex,

        return None  # if no node was added

    def getOwner(self):
        return self.owner

    def getNode(self, index):
        return self.nodes[index]

    def size(self):
        return len(self.nodes)