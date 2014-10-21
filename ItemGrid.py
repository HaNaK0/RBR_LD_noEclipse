"""
Created on 19 aug 2014

@author: HaNaK0
"""
import tkinter as tk
import constants as con
import Path as pa


class ItemGrid(object):
    """
    The grid that contains all objects placed on screen
    """

    def __init__(self, workspace, sprites):
        """
        Constructor
        """
        self.currentSelected = None
        self.sprites = sprites
        self.workspace = workspace
        self.grid = []
        for i in range(int(workspace.width / workspace.gridX)):
            temp_list = []
            for j in range(int(workspace.height / workspace.gridY)):
                temp_list.append(None)
            self.grid.append(temp_list)
        self.paths = []
        self.currentPath = None

    def add(self, posGridX, posGridY, objType=con.OTYPE["BASIC"]):

        # if empty
        if self.grid[posGridX][posGridY] is None:
            #self.grid[posGridX][posGridY] = WorkspaceItem(self.workspace, self.sprites, posGridX, posGridY)
            #adds a basic block
            if objType == con.OTYPE["BASIC"]:
                self.grid[posGridX][posGridY] = WorkspaceItem(self.workspace, self.sprites, posGridX, posGridY)

            #adds a player
            elif objType == con.OTYPE["PLAYER"]:
                self.grid[posGridX][posGridY] = PlayerItem(self.workspace, self.sprites, posGridX, posGridY)

            #adds a enemy spike
            elif objType == con.OTYPE["SPIKE"]:
                self.grid[posGridX][posGridY] = EnemySpikeItem(self.workspace, self.sprites, posGridX, posGridY)

            #adds a flying enemy blob
            elif objType == con.OTYPE["BLOB_FLY"]:
                self.grid[posGridX][posGridY] = EnemyBlobFlying(self.workspace, self.sprites, posGridX, posGridY)

            #adds a walking enemy blob
            elif objType == con.OTYPE["BLOB_WALK"]:
                self.grid[posGridX][posGridY] = EnemyBlobWalking(self.workspace, self.sprites, posGridX, posGridY)

            #adds a NE half block
            elif objType == con.OTYPE["HALF_B_NE"]:
                self.grid[posGridX][posGridY] = HalfBlockNE(self.workspace, self.sprites, posGridX, posGridY)

            #adds a NW half block
            elif objType == con.OTYPE["HALF_B_NW"]:
                self.grid[posGridX][posGridY] = HalfBlockNW(self.workspace, self.sprites, posGridX, posGridY)

            #adds a SE half block
            elif objType == con.OTYPE["HALF_B_SE"]:
                self.grid[posGridX][posGridY] = HalfBlockSE(self.workspace, self.sprites, posGridX, posGridY)

            #adds a SW half block
            elif objType == con.OTYPE["HALF_B_SW"]:
                self.grid[posGridX][posGridY] = HalfBlockSW(self.workspace, self.sprites, posGridX, posGridY)

            #adds a pathing Node
            elif objType == con.OTYPE["PATH_POINT"]:
                self.grid[posGridX][posGridY] = PathPoint(self.workspace, self.sprites, posGridX, posGridY, self)

    def remove(self, posGridX, posGridY):
        """
        removes a workspace item from itemGrid
        """
        if self.grid[posGridX][posGridY] is not None:
            self.grid[posGridX][posGridY].removeObj()
            self.grid[posGridX][posGridY] = None
        else:
            print("empty")

    def get(self, posGridX, posGridY):
        """
        gets a workspace item based on position in grid
        """
        return self.grid[posGridX][posGridY]

    # select an object
    def select(self, posGridX, posGridY):
        if self.currentSelected is not None:  # if an item is selected
            self.currentSelected.selectToggle()  # deselect it

        if self.grid[posGridX][posGridY] is not None:  # if clicked space contains an item

            self.currentSelected = self.grid[posGridX][posGridY]

            self.currentSelected.selectToggle()
        else:
            self.currentSelected = None

    def getSelected(self):
        return self.currentSelected

    def addPath(self, owner):
        tempPath = pa.Path(len(self.paths), owner)
        self.paths.append(tempPath)
        return tempPath


class WorkspaceItem(object):
    """
    Level Object class
    parent object for all objects that are able to be placed in a level
    """
    OTYPE = con.OTYPE["BASIC"]

    def __init__(self, workspace, sprites, posGridX, posGridY):
        self.workspace = workspace
        self.selected = False
        self.posGridX = posGridX
        self.posGridY = posGridY
        self.selectSquare = None

        self.canvasItem = workspace.canvas.create_image(self.posGridX * workspace.gridX + workspace.offsetX,
                                                        self.posGridY * workspace.gridY + workspace.offsetY,
                                                        image=sprites[self.OTYPE],
                                                        tags="object",
                                                        anchor=tk.NW)

    def removeObj(self):
        """
        removes the canvas item
        """
        self.workspace.canvas.delete(self.canvasItem)

    def selectToggle(self):
        print("toggle")
        if not self.selected:
            self.selectSquare = self.workspace.canvas.create_rectangle(self.posGridX * self.workspace.gridX,
                                                                       self.posGridY * self.workspace.gridY,
                                                                       self.posGridX * self.workspace.gridX +
                                                                       self.workspace.gridX,
                                                                       self.posGridY * self.workspace.gridY +
                                                                       self.workspace.gridY,
                                                                       outline='blue')
            self.selected = True
        else:
            self.workspace.canvas.delete(self.selectSquare)
            self.selected = False

    def getType(self):
        """
        to get the item type
        @return: the OTYPE constant int
        """
        return self.OTYPE


class BlockItem(WorkspaceItem):
    """
    Basic block tile item class
    A basic 32x32 tile
    
    """


class PlayerItem(WorkspaceItem):
    """
    Player item to represent where the player will start in the level
    """
    OTYPE = con.OTYPE["PLAYER"]


class EnemySpikeItem(WorkspaceItem):
    """
    A spike enemy item
    """
    OTYPE = con.OTYPE["SPIKE"]


class EnemyBlobFlying(WorkspaceItem):
    """
    A blob flying around
    @todo: pathing
    """
    OTYPE = con.OTYPE["BLOB_FLY"]

    def __init__(self, workspace, sprites, posGridX, posGridY, ):
        super().__init__(workspace, sprites, posGridX, posGridY)

        self.path = None

    def setPath(self, path):
        self.path = path

    def removeObj(self):
        super(EnemyBlobFlying, self).removeObj()

        if self.path is not None:
            for i in self.path.nodes:
                i.removeObj()


class EnemyBlobWalking(EnemyBlobFlying):
    """
    A blob walking around
    """
    OTYPE = con.OTYPE["BLOB_WALK"]


class HalfBlockNE(WorkspaceItem):
    """
    A basic half block turned to the upper right corner
    """
    OTYPE = con.OTYPE["HALF_B_NE"]


class HalfBlockNW(WorkspaceItem):
    """
    A basic half block turned to the upper left corner 
    """
    OTYPE = con.OTYPE["HALF_B_NW"]


class HalfBlockSE(WorkspaceItem):
    """
    A basic half block turned to the lower right corner
    """
    OTYPE = con.OTYPE["HALF_B_SE"]


class HalfBlockSW(WorkspaceItem):
    """
    A basic half block turned to the lower left corner
    """
    OTYPE = con.OTYPE["HALF_B_SW"]


class PathPoint(WorkspaceItem):
    """
    A path point that displays the path of a mob
    """
    OTYPE = con.OTYPE["PATH_POINT"]

    def __init__(self, workspace, sprites, posGridX, posGridY, itemGrid):
        super(PathPoint, self).__init__(workspace, sprites, posGridX, posGridY)

        if itemGrid.currentSelected.path is None:
            itemGrid.currentSelected.setPath(itemGrid.addPath(itemGrid.currentSelected))

        self.path = itemGrid.currentSelected.path
        self.index = self.path.add(self)
        self.line = None

        if self.index is not None and self.path.size() > 1:
            temp = self.path.getNode(self.index - 1)
            self.line = self.workspace.canvas.create_line(temp.posGridX * 32 + 16, temp.posGridY * 32 + 16,
                                                          self.posGridX * 32 + 16, self.posGridY * 32 + 16,
                                                          fill='yellow')

    def removeObj(self):
        super(PathPoint, self).removeObj()
        self.workspace.canvas.delete(self.line)