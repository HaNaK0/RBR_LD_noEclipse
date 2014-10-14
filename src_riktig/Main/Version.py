"""
Created on 12 aug 2014

@author: HaNaK0
"""


class Version(object):
    """
    handles version of a program and compare it to a string in the format xx.xx
    """

    def __init__(self, aVersion):
        """
        Constructor
        gets the version and stores it
        """
        
        self.version = aVersion
        
    def __str__(self):
        rep = self.version
        return rep
        
    def compare(self, aVersion):
        """compare a version string to current version"""
        if int(aVersion[0:2]) == int(self.version[0:2]):
            if int(aVersion[3:5]) == int(self.version[3:5]):
                return "current"
            elif int(aVersion[3:5]) < int(self.version[3:5]):
                return "old"
            elif int(aVersion[3:5]) > int(self.version[3:5]):
                return "future"
        else:
            return "incompatible"