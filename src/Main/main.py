'''
Created on 12 aug 2014

@author: HaNaK0
'''
import tkinter as tk
import widgets
import workspace as ws
import constants as con
from tkinter import filedialog as fd
import dialogs as dl

class Main (object):
    
    def __init__(self):
        self.workspace = None #ws.Workspace(self.root, widgets.StatusBar(self.root, images), images, gridX = 32, gridY = 32, width = 1920 * 3, height = 1080)
        self.root = tk.Tk()
        self.images = ws.loadImages()
        self.root.config(menu = widgets.MenuBarC(self.root, self.images, self.newDialog, self.loadWorkSpace))
        self.root.geometry("600x600")
        self.root.title("RBR_LD")
        self.root.mainloop()
        self.inDict = {"width" : 0, "height" : 0, "gridX" : 32, "gridY" : 32}

    
    def newDialog(self):
        '''
        Opens up the New Project Dialog window
        '''
        dl.NewProject(self.root, self)
    
    
    def newWorkSpace(self):
        
        if self.workspace == None:
            self.workspace = ws.Workspace(self.root, widgets.StatusBar(self.root, self.images), self.images, gridX = self.inDict["gridX"], gridY = self.inDict["gridY"], width = self.inDict["width"], height = self.inDict["height"])
            self.root.config(menu = widgets.MenuBar(self.root, self.workspace, self.images, self.newWorkSpace, self.loadWorkSpace))
        else:
            self.workspace.destroy()
            self.workspace = ws.Workspace(self.root, widgets.StatusBar(self.root, self.images), self.images, gridX = self.inDict["gridX"], gridY = self.inDict["gridY"], width = self.inDict["width"], height = self.inDict["height"])
            self.root.config(menu = widgets.MenuBar(self.root, self.workspace, self.images, self.newWorkSpace, self.loadWorkSpace))
            
    def loadWorkSpace(self):
        
        if self.workspace == None:
            self.workspace = ws.Workspace(self.root, widgets.StatusBar(self.root, self.images), self.images, gridX = 32, gridY = 32, width = 1920 * 3, height = 1080, option = con.WCC["LOAD"], 
                                          file = fd.askopenfilename(parent = self.root, defaultextension = ".blml", title = "Open", filetypes=[("rbr level file", ".blml"), ("All files", ".*")]))
            self.root.config(menu = widgets.MenuBar(self.root, self.workspace, self.images, self.newWorkSpace, self.loadWorkSpace))
        else:
            self.workspace.destroy()
            self.workspace = ws.Workspace(self.root, widgets.StatusBar(self.root, self.images), self.images, gridX = 32, gridY = 32, width = 1920 * 3, height = 1080, option = con.WCC["LOAD"], 
                                          file = fd.askopenfilename(parent = self.root, defaultextension = ".blml", title = "Open", filetypes=[("rbr level file", ".blml"), ("All files", ".*")]))
            self.root.config(menu = widgets.MenuBar(self.root, self.workspace, self.images, self.newWorkSpace, self.loadWorkSpace))
            