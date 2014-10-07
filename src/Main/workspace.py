'''
Created on 13 aug 2014

@author: HaNaK0
'''
import tkinter as tk
from tkinter import filedialog as fd
import ItemGrid as ig
import ActionStack as As
import constants as con
import xml.etree.ElementTree as et

# constructor options constants
#NEW = 'new'
#LOAD = 'load'

# Tool Constants
#MOVE = 'Move'
#SELECT = 'Select'
#ERASE = 'Erase'
#PLACE = 'Place'

# levelObject types constants
#BASIC = 0
        
class Workspace(object):
    '''
    the workspace 
    contains a canvass widget
    '''
    
    def __init__(self, canvasMaster, statuslBar, images, option = con.WCC["NEW"], width = 608, height = 288, gridX = 32, gridY = 32, file = None):
        '''
        constructor
        creates a canvas and gives it canvas Master
        option is one of the constants NEW or LOAD
        if New it calls create new and gives it int width, int height, int gridX, int gridY
        if Load it calls loadWork and gives it string file
        '''
        #loading images
        self.sprites = images
        
        #setting status bar
        self.statusBar = statuslBar
        
        #creating actionStack 
        self.actionStack = As.ActionStack(self)
        
        #setting values
        self.currentTool = con.TOOL["MOVE"]
        self.statusBar.setToolModeLbl(self.currentTool)
        self.currentItemType = 0
        self.file = file
        
        #setting up the canvas
        self.root = canvasMaster
        self.canvas = tk.Canvas(canvasMaster)
        self.canvas.pack(fill = tk.BOTH, expand = True)
        
        self.canvas.focus_set()
        #binding events 
        #Mouse event handlers
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.move)
        self.canvas.bind("<ButtonRelease-1>", self.release)
        
        #Mouse position event handler
        self.canvas.bind("<Motion>", self.statusBar.setMouseLbl)
        
        #Mouse wheel event
        self.canvas.bind("<MouseWheel>", self.scroll)
        
        #Button events handler
        #changing tool
        self.canvas.bind("q", self.setToMove)
        self.canvas.bind("w", self.setToSelect)
        self.canvas.bind("e", self.setToPlace)
        self.canvas.bind("r", self.setToErase)
        
        #Save events
        self.canvas.bind("<Control-s>", self.save)
        
        #Edit event
        self.canvas.bind("<Control-z>", self.actionStack.undo)
        self.canvas.bind("<Control-y>", self.actionStack.redo)
                
        self.moveOriginX = 0
        self.moveOriginY = 0
        
        self.offsetX = 0
        self.offsetY = 0
         
        #if new or load
        if option == con.WCC["NEW"]:
            self.createNew(width, height, gridX, gridY)
        elif option == con.WCC["LOAD"]:
            self.load(file)
            
         
    
    def createNew(self, width, height, gridX, gridY):
        '''
        creates a new workspace and places a grid in it
        and sets up variables
        '''
        #setting up correct values
        self.width = width
        self.height = height
        
        self.gridX = gridX
        self.gridY = gridY
                
        #creating grid
        for i in range(int(self.width / self.gridX)):
            self.canvas.create_line(i * self.gridX, 0, i * self.gridX, self.height, tags = "Grid")
            
        for i in range(int(self.height / self.gridY)):
            self.canvas.create_line(0, i * self.gridY, self.width, i * self.gridY, tags = "Grid")
            
        #creating ItemGrid
        self.itemGrid = ig.ItemGrid(self, self.sprites)
    
    
    def load(self, file, event = None):
        '''
        loads a file and creates the set the variables for the grid
        '''
        tree = et.ElementTree(file = file)
        root = tree.getroot()
        gridEl = root.find("grid")
        items = gridEl.findall("item")
        
        #setting up correct values
        self.width = int(gridEl.get("width"))
        self.height = int(gridEl.get("height"))
        
        self.gridX = int(gridEl.get("gridX"))
        self.gridY = int(gridEl.get("gridY"))
                
        #creating grid
        for i in range(int(self.width / self.gridX)):
            self.canvas.create_line(i * self.gridX, 0, i * self.gridX, self.height, tags = "Grid")
            
        for i in range(int(self.height / self.gridY)):
            self.canvas.create_line(0, i * self.gridY, self.width, i * self.gridY, tags = "Grid")
            
        #creating ItemGrid
        self.itemGrid = ig.ItemGrid(self, self.sprites)
        
        for i in items:
            self.itemGrid.add(int(i.get("x")), int(i.get("y")), con.OTYPE[i.get("iType")])
            
            
        
    def destroy(self):
        self.canvas.destroy()       
    
    
    
    #event callback
    #canvas event <Button-1>        
    def click(self, event):
        '''
        takes care of what happens when mouse button 1 is clicked
        '''
        if self.currentTool == con.TOOL["MOVE"]:
            #sets the origin value to begin movement 
            #and the start value to keep track of offset
            self.moveOriginX = event.x
            self.moveOriginY = event.y
            self.moveStartX = event.x
            self.moveStartY = event.y
        elif self.currentTool == con.TOOL["PLACE"]:
            #creates a level object at event.x, event.y
            self.createWorkSpItem(event.x, event.y)
        elif self.currentTool == con.TOOL["ERASE"]:
            #destroys the object at event.x, event.y
            self.removeWorkSpItem(event.x, event.y)
    
    
    
    #canvas event <B1-Motion>    
    def move(self, event):
        '''
        takes care of what happens if mouse button 1 held down and moved
        '''
        self.statusBar.setMouseLbl(event)
        
        if self.currentTool == con.TOOL["MOVE"]:
            #moves the distance the mouse moved since last update 
            self.canvas.move(tk.ALL, event.x - self.moveOriginX, event.y - self.moveOriginY)
            #sets origin so movement becomes same as mouse
            self.moveOriginX = event.x
            self.moveOriginY = event.y
    
    
    
    #canvas event <ButtonReleas-1>        
    def release(self, event):
        '''
        take cares of what happens when the mouse button 1 is released
        '''
        if self.currentTool == con.TOOL["MOVE"]:
            self.offsetX += event.x - self.moveStartX
            self.offsetY += event.y - self.moveStartY
            
    #canvas event <MouseWheel>
    def scroll(self, event):
        '''
        takes care of scrolling with the mouse wheel
        '''
        if event.delta > 0:
            self.currentItemType += 1
            if self.currentItemType >=  9:
                self.currentItemType = 0
        else:
            self.currentItemType -= 1
            if self.currentItemType < 0:
                self.currentItemType = 8
            
        self.statusBar.setScrollLbl(self.currentItemType)
    
    #canvas event 'q'        
    def setToMove(self, event):
        '''
        Set tool to Move
        '''
        self.currentTool = con.TOOL["MOVE"]
        self.statusBar.setToolModeLbl(self.currentTool)
        
    
    #canvas event 'w'
    def setToSelect(self, event):
        '''
        set tool to Select
        '''
        self.currentTool = con.TOOL["SELECT"]
        self.statusBar.setToolModeLbl(self.currentTool)
        
        
    #canvas event 'e'
    def setToPlace(self, event):
        '''
        set tool to place
        '''
        self.currentTool = con.TOOL["PLACE"]
        self.statusBar.setToolModeLbl(self.currentTool)
        
    
    #canvas event 'r'
    def setToErase(self, event):
        '''
        set tool to erase
        '''
        self.currentTool = con.TOOL["ERASE"]
        self.statusBar.setToolModeLbl(self.currentTool)
        
        
    #creating WorkspaceItems
    def createWorkSpItem(self, X, Y):    
        '''
        creating level object in canvas
        '''
        posGridX = int((X - self.offsetX) / self.gridX)
        posGridY = int((Y - self.offsetY) / self.gridY)
        
        #Make sure new position is in grid
        if posGridX > ((self.width - self.width % self.gridX) / self.gridX) - 1:
            posGridX = int(((self.width - self.width % self.gridX) / self.gridX) -1)
        elif posGridX < 0:
            posGridX = 0
            
        if posGridY > ((self.height - self.height % self.gridY) / self.gridY)-1:
            posGridY = int(((self.height - self.height % self.gridY) / self.gridY) -1)
        elif posGridY < 0:
            posGridY = 0
        
        #create the object
        self.actionStack.actionCreate(posGridX, posGridY, self.currentItemType)
    
    #removing WorkspaceItems
    def removeWorkSpItem(self, X, Y):
        posGridX = int((X - self.offsetX) / self.gridX)
        posGridY = int((Y - self.offsetY) / self.gridY)
        
        #if coordinates are in range of grid
        if posGridX <= ((self.width - self.width % self.gridX) / self.gridX) - 1 and posGridX >= 0 and posGridY <= ((self.height - self.height % self.gridY) / self.gridY)-1 and posGridY >= 0:
            if self.itemGrid.get(posGridX, posGridY) != None:
                self.actionStack.actionDestroy(posGridX, posGridY)
        else:
            print("out of range")
            
    def saveAs(self, event = None):
        '''
        opens a dialog in which you are able too choose where to save your file
        '''
        temp_file = self.file
        self.file = ""
        
        self.file = fd.asksaveasfilename(parent = self.root, defaultextension = ".blml", title = "Save As", filetypes=[("rbr level file", "*.blml"), ("All files", "*.*")])
        
        if self.file == "":
            self.file = temp_file
            return
        
        self.save()
        
        
    def save(self, event = None):
        '''
        if already saved it saves in last location 
        otherwise it calls the save as method
        '''
        if self.file == None:
            self.saveAs()
        
        root = et.Element("blml", {"version" : str(0.1)})
        
        grid = et.SubElement(root, "grid", {"height" : str(self.height), "width" : str(self.width), "gridX" : str(self.gridX), "gridY" : str(self.gridY)}) 
        
        gridWidth = self.width / self.gridX
        gridHeight = self.height / self.gridY
        
        for i in range(int(gridWidth)):
            for j in range(int(gridHeight)):
                if self.itemGrid.get(i, j) == None:
                    continue
                else:
                    et.SubElement(grid, "item", {"iType" : con.ROTYPE[self.itemGrid.get(i, j).OTYPE], "x" : str(i), "y" : str(j)})
                
        tree = et.ElementTree(root)
        
        #fileO = open(self.file, 'w')
        tree.write(self.file, xml_declaration = True)
        #fileO.close()
        
    
        
        
            
def loadImages():
    '''
    @return: a Tuple of image objects: (simpleTile, player, spike, blob_fly, blob_walk, block_half_NE, block_half_NW, block_half_SE, block_half_SW)
    contains:
    [0]: simpleTile
    [1]: player
    [2]: enemy_spike
    [3]: enemy_blob_flying
    [4]: enemy_blob_walking
    [5]: block_half_NE
    [6]: block_half_NW
    [7]: block_half_SE
    [8]: block_half_SW
    '''
    #Temporary block sprite
    try:
        simpleTile = tk.PhotoImage(file = "..\Main\Sprites\\temp_block_32x32.ppm")
    except tk.TclError as e:
        print(e)
        simpleTile = None
    
    #Bob sprite
    try:
        player = tk.PhotoImage(file = "..\Main\Sprites\Bob_animation_ball_1.gif")
    except tk.TclError as e:
        print(e)
        player = None
    
    #Spike enemy sprite    
    try:
        spike = tk.PhotoImage(file = "..\Main\Sprites\\temp_spike.ppm")
    except tk.TclError as e:
        print(e)
        spike = None
    
    #enemy Blob flying    
    try:
        blob_fly = tk.PhotoImage(file = "..\Main\Sprites\enemy_blob_flying.ppm")
    except tk.TclError as e:
        print(e)
        blob_fly = None
    
    #enemy blob walking
    try:
        blob_walk = tk.PhotoImage(file = "..\Main\Sprites\enemy_blob_walking.ppm")
    except tk.TclError as e:
        print(e)
        blob_walk = None
    
    #half block NE    
    try:
        block_half_NE = tk.PhotoImage(file = "..\Main\Sprites\\temp_block_half_NE.ppm")
    except tk.TclError as e:
        print(e)
        block_half_NE = None
    
    #half block NW    
    try:
        block_half_NW = tk.PhotoImage(file = "..\Main\Sprites\\temp_block_half_NW.ppm")
    except tk.TclError as e:
        print(e)
        block_half_NW = None
    
    #half block SE    
    try:
        block_half_SE = tk.PhotoImage(file = "..\Main\Sprites\\temp_block_half_SE.ppm")
    except tk.TclError as e:
        print(e)
        block_half_SE = None
    
    #half block SW    
    try:
        block_half_SW = tk.PhotoImage(file = "..\Main\Sprites\\temp_block_half_SW.ppm")
    except tk.TclError as e:
        print(e)
        block_half_SW = None
    
    sprT = (simpleTile, player, spike, blob_fly, blob_walk, block_half_NE, block_half_NW, block_half_SE, block_half_SW)
        
    return sprT
