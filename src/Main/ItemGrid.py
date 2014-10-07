'''
Created on 19 aug 2014

@author: HaNaK0
'''
import tkinter as tk
import constants as con


# levelObject types constants


class ItemGrid(object):
    '''
    The grid that contains all objects placed on screen
    '''

    def __init__(self, workspace, sprites):
        '''
        Constructor
        '''
        self.currentSelected = None
        self.sprites = sprites
        self.workspace = workspace
        self.grid = []
        for i in range(int(workspace.width / workspace.gridX)):
            temp_list = []
            for i in range(int(workspace.height / workspace.gridY)):
                temp_list.append(None)
            self.grid.append(temp_list)
        
        
        
    def add(self,posGridX, posGridY, objType = con.OTYPE["BASIC"]):
        print("does")
        
        #if empty
        if self.grid[posGridX][posGridY] == None:
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
    
        
    def remove(self, posGridX, posGridY):
        if not self.grid[posGridX][posGridY] == None:
            self.grid[posGridX][posGridY].removeObj()
            self.grid[posGridX][posGridY] = None
        else:
            print("empty")

    def get(self, posGridX, posGridY):
        return self.grid[posGridX][posGridY]
    
    
    def select(self, posGridX, posGridY):
        if self.currentSelected != None:
            self.currentSelected.selectToggle()
            
        if self.grid[posGridX][posGridY] != None:
            self.currentSelected = self.grid[posGridX][posGridY]
            
            self.currentSelected.selectToggle()
        else:
            self.currentSelected = None
            



class WorkspaceItem(object):
    '''
    Level Object class
    parent object for all objects that are able to be placed in a level
    '''
    OTYPE = con.OTYPE["BASIC"]
    def __init__(self, workspace, sprites, posGridX, posGridY):
        self.workspace = workspace
        self.selected = False
        self.posGridX = posGridX
        self.posGridY = posGridY
         
        self.canvasItem = workspace.canvas.create_image(self.posGridX * workspace.gridX + workspace.offsetX, self.posGridY * workspace.gridY + workspace.offsetY,
                                                         image = sprites[self.OTYPE],
                                                         tags = "object",
                                                         anchor = tk.NW)
        
    
    def removeObj(self):
        '''
        removes the canvas item
        '''
        self.workspace.canvas.delete(self.canvasItem)
    
    
        
    def selectToggle(self):
        if self.selected == False:
            self.selected = True
        else:
            self.selected = False



class BlockItem(WorkspaceItem):
    '''
    Basic block tile item class
    A basic 32x32 tile
    
    '''
    
class PlayerItem(WorkspaceItem):
    '''
    Player item to represent where the player will start in the level
    '''
    OTYPE = con.OTYPE["PLAYER"]
    
class EnemySpikeItem(WorkspaceItem):
    '''
    A spike enemy item
    '''
    OTYPE = con.OTYPE["SPIKE"]
    
class EnemyBlobFlying(WorkspaceItem):
    '''
    A blob flying around
    @todo: pathing
    '''
    OTYPE = con.OTYPE["BLOB_FLY"]
    
class EnemyBlobWalking(WorkspaceItem):
    '''
    A blob walking around
    @todo: pathing
    '''
    OTYPE = con.OTYPE["BLOB_WALK"]
    
class HalfBlockNE(WorkspaceItem):
    '''
    A basic half block turned to the upper right corner
    '''
    OTYPE = con.OTYPE["HALF_B_NE"]
    
class HalfBlockNW(WorkspaceItem):
    '''
    A basic half block turned to the upper left corner 
    '''
    OTYPE = con.OTYPE["HALF_B_NW"]
    
class HalfBlockSE(WorkspaceItem):
    '''
    A basic half block turned to the lower right corner
    '''
    OTYPE = con.OTYPE["HALF_B_SE"]
    
class HalfBlockSW(WorkspaceItem):
    '''
    A basic half block turned to the lower left corner
    '''
    OTYPE = con.OTYPE["HALF_B_SW"]