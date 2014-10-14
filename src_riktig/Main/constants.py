"""
Created on 9 sep 2014

@author: HaNaK0
"""
#type constants
OTYPE = {"BASIC" : 0, "PLAYER" : 1, "SPIKE" : 2, "BLOB_FLY" : 3, "BLOB_WALK" : 4, "HALF_B_NE" : 5, "HALF_B_NW" : 6, "HALF_B_SE" : 7, "HALF_B_SW" : 8, "PATH_POINT" : 9}
ROTYPE = {0 : "BASIC", 1 : "PLAYER", 2 : "BLOB_FLY", 3 : "BLOB_FLY", 4 : "BLOB_WALK", 5 : "HALF_B_NE", 6 : "HALF_B_NW", 7 : "HALF_B_SE", 8 : "HALF_B_SW", 9 : "PATH_POINT"}

#tool constants
TOOL = {"MOVE" : 'Move', "SELECT": 'Select', "ERASE" : 'Erase', "PLACE" : 'Place'}

#workspace constructor constants
WCC = {"NEW" : 'New', "LOAD" : 'Load'}

#Pathing Mode constants
PMC = {"OFF": 0, "FLYING" : 1, "WALKING": 2}