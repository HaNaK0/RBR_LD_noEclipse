"""
Created on 19 aug 2014

@author: HaNaK0
"""

#constants
BASIC = 0


class ActionStack(object):
    """
    a stack to contain actions
    """
    def __init__(self, workspace):
        self.workspace = workspace
        self.stack = []
        self.undos = 0
    
    #create a basic workspace item and an actionObject for it    
    def actionCreate(self, posGridX, posGridY, oType=BASIC):
        if self.undos > 0:
            del self.stack[len(self.stack) - self.undos:]
            self.undos = 0
            
        self.stack.append(ActionCreate(self.workspace, posGridX, posGridY, oType))
    
    #deletes a workspace item an creates an actionObject for it
    def actionDestroy(self, posGridX, posGridY):
        if self.undos > 0:
            del self.stack[len(self.stack) - self.undos:]
            self.undos = 0
        
        self.stack.append(ActionDestroy(self.workspace, posGridX, posGridY))
    
    #undoes an action    
    def undo(self, event=None):
        if self.stack and self.undos < len(self.stack):
            print(event)
            print(len(self.stack) - 1 - self.undos)
            self.stack[len(self.stack) - 1 - self.undos].undo()
            self.undos += 1
            print("undo")
        else:
            print("Nothing more to undo!")

    #re does an action        
    def redo(self, event=None):
        if self.stack and self.undos > 0:
            print(event)
            print(len(self.stack) - 1 - self.undos)
            self.stack[len(self.stack) - 1 - self.undos + 1].redo()
            self.undos -= 1
        else:
            print("nothing to re do")


class Action(object):
    """
    Base class
    """
    def __init__(self, workspace, posGridX, posGridY):
        self.workspace = workspace
        self.posGridX = posGridX
        self.posGridY = posGridY
        self.active = True
        print("Action")
    
    #undo    
    def undo(self):
        if self.active:
            self.active = False
        else:
            print("Error: Sollux")
    
    #re do
    def redo(self):
        if not self.active:
            self.active = True
        else:
            print("Error: Sollux")


class ActionDestroy(Action):
    """
    instatiated when anything is removed from the canvas
    """
    def __init__(self, workspace, posGridX, posGridY):
        super(ActionDestroy, self).__init__(workspace, posGridX, posGridY)
        self.oType = self.workspace.itemGrid.get(posGridX, posGridY).OTYPE
        
        self.workspace.itemGrid.remove(self.posGridX, self.posGridY)
    
    #undo
    def undo(self):
        if self.active:
            self.workspace.itemGrid.add(self.posGridX, self.posGridY, objType=self.oType)
            self.active = False
        else:
            print("Error: Sollux")
    
    #redo        
    def redo(self):
        if not self.active:
            self.active = True
            self.workspace.itemGrid.remove(self.posGridX, self.posGridY)
        else:
            print("Error: Mituna")


class ActionCreate(Action):
    """
    instantiated when anything is created in the canvas
    """
    def __init__(self, workspace, posGridX, posGridY, oType):
        super(ActionCreate, self).__init__(workspace, posGridX, posGridY)
        self.oType = oType
        
        workspace.itemGrid.add(self.posGridX, self.posGridY, objType=self.oType)
    
    #undo
    def undo(self):
        """done"""
        if self.active:
            self.workspace.itemGrid.remove(self.posGridX, self.posGridY)
            self.active = False
        else:
            print("Error: Sollux")
            
    #re do
    def redo(self):
        if not self.active:
            self.workspace.itemGrid.add(self.posGridX, self.posGridY, objType=self.oType)
            self.active = True
        else:
            print("Error: Mituna")