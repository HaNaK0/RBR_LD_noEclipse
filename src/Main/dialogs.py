'''
Created on 30 sep 2014

@author: HaNaK0
'''
import tkinter as tk


class NewProject(tk.Toplevel):
    '''
    A new project dialog 
    '''


    def __init__(self, master, main):
        '''
        Constructor
        '''
        super(NewProject, self).__init__(master)
        self.grid()
        
        #height and width labels
        tk.Label(self, text = "Width:").grid(row = 0, column = 0, sticky =tk.W)
        tk.Label(self, text = "Height:").grid(row = 1, column = 0, sticky =tk.W)
        
        #height and width spin boxes
        
        wbVar = tk.StringVar(self)
        wbVar.set(5760)
        self.widthBox = tk.Spinbox(self, textvariable = wbVar, from_ = 0, to = 1000000, increment = 1)
        self.widthBox.grid(row = 0, column = 1, sticky = tk.W)
        
        hbVar = tk.StringVar(self)
        hbVar.set(1080)
        self.heightBox = tk.Spinbox(self, textvariable = hbVar, from_ = 0, to = 1000000, increment = 1)
        self.heightBox.grid(row = 1, column = 1, sticky = tk.W)
        
        #grid X and grid Y labels
        tk.Label(self, text = "the height and width of every cell in the grid.").grid(row = 3, column = 0, columnspan = 2, sticky = tk.W)
        
        tk.Label(self, text = "Grid X").grid(row = 4, column = 0, sticky = tk.W)
        tk.Label(self, text = "Grid Y").grid(row = 5, column = 0, sticky = tk.W)
        
        #grid X and grid Y spin boxes
        gxVar = tk.StringVar(self)
        gxVar.set(32)
        self.gridXBox = tk.Spinbox(self, textvariable = gxVar, from_ = 0, to = 10000, increment = 1)
        self.gridXBox.grid(row = 4, column = 1, sticky = tk.W)
        
        gyVar = tk.StringVar(self)
        gyVar.set(32)
        self.gridYBox = tk.Spinbox(self, textvariable = gyVar, from_ = 0, to = 10000, increment = 1)
        self.gridYBox.grid(row = 5, column = 1, sticky = tk.W)
        
        #finish button
        self.button = tk.Button(self, text = "Ok", command = self.okButtonPressed).grid(row = 6, column = 0, sticky = tk.W)
        self.button = tk.Button(self, text = "Cancel", command = self.cancelButtonPressed).grid(row = 6, column = 1, sticky = tk.W)
        
        self.main = main
        self.title("New")
        self.mainloop()
        
    def okButtonPressed(self):
        '''
        gets called when the Ok button on the new project dialog are pressed 
        '''
        self.main.inDict["width"] = int(self.widthBox.get())
        self.main.inDict["height"] = int(self.heightBox.get())
        
        self.main.inDict["gridX"] = int(self.gridXBox.get())
        self.main.inDict["gridY"] = int(self.gridYBox.get())
        self.destroy()
        
        self.main.newWorkSpace()
        
    def cancelButtonPressed(self):
        self.destroy()
        
      
      
      
  
        
class OptionsDilaog(tk.Toplevel):
    '''
    An options dialog
    a dialog where you change the program preferences
    '''
    
    def __init__(self, master, controlDict):
        '''
        The constructor
        '''
        super(OptionsDilaog, self).__init__(master)
        self.grid()
        
        #controls 
        tk.Label(self, text = "Controls").grid(row = 0, column = 0, columnSpan = 3, sticky = tk.W)
        
        #Move
        
        