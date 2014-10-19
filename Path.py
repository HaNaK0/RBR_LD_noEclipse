__author__ = 'HaNaK0'

import constants as con
import ItemGrid as ig


class Path(object):
    """
    path instances to keep track of paths
    """
    def __init__(self, index, pType):
        """
        Init
        :return:
        """
        self.index = index
        self.nodes = []
        self.pType = pType

    def add(self, node: ig.PathPoint):
        """
        adds a node to the path
        :param node: a node workspace item
        :return: index, path index
        """
        if self.pType == con.PMC["WALKING"]:
            if len(self.nodes) == 0:
                self.nodes.append(node)
                return 0, self.index
            elif len(self.nodes) == 1:
                if node.posGridX > self.nodes[0].posGridX:
                    self.nodes.append(node)
                    return 1, self.index
                else:
                    self.nodes.append(self.nodes[0])
                    self.nodes[0] = node
                    return 0, self.index
            elif len(self.nodes) == 2:
                if node.posGridX < self.nodes[0].posGridX:
                    self.nodes = node
                    return 0, self.index
                elif node.posGridX > self.nodes[1].posGridX:
                    self.nodes.append