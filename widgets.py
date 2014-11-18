"""
Created on 12 aug 2014

@author: HaNaK0
"""
import tkinter as tk


class MenuBar(tk.Menu):
    """
    The menu bar for the root window
    inherits from tkinter.Menu
    """

    def __init__(self, master, workspace, images, newCall, loadCall):
        """
        Constructor
        """
        super(MenuBar, self).__init__(master)

        self.createMenu(workspace, newCall, loadCall)

    def createMenu(self, workspace, newCall, loadCall):
        """
        create the menu bar and all cascades in it
        """
        # File menu
        fileMenu = tk.Menu(self, tearoff=0)
        fileMenu.add_command(label="New", command=newCall)
        fileMenu.add_command(label="Open", command=loadCall)
        fileMenu.add_separator()
        fileMenu.add_command(label="Save", command=workspace.save)
        fileMenu.add_command(label="Save As", command=workspace.saveAs)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit")  # command=Exit method
        self.add_cascade(label="File", menu=fileMenu)

        # Edit Menu
        editMenu = tk.Menu(self, tearoff=0)
        editMenu.add_command(label="Undo", command=workspace.actionStack.undo)
        editMenu.add_command(label="Redo", command=workspace.actionStack.redo)
        self.add_cascade(label="Edit", menu=editMenu)

        # Run Menu
        runMenu = tk.Menu(self, tearoff=0)
        runMenu.add_command(label="Run")  # command=Run method
        self.add_cascade(label="Run", menu=runMenu)

        # Help menu
        helpMenu = tk.Menu(self, tearoff=0)
        helpMenu.add_command(label="Settings")  # settings window
        self.add_cascade(label="Help", menu=helpMenu)


class MenuBarC(tk.Menu):
    """
    The menu bar for the root window when no workspace is open
    inherits from tkinter.Menu
    """

    def __init__(self, master, images, newCall, loadCall):
        """
        Constructor
        """
        super(MenuBarC, self).__init__(master)

        self.createMenu(newCall, loadCall)

    def createMenu(self, newCall, loadCall):
        """
        create the menu bar and all cascades in it
        """
        # File menu
        fileMenu = tk.Menu(self, tearoff=0)
        fileMenu.add_command(label="New", command=newCall)  # command=New project method
        fileMenu.add_command(label="Open", command=loadCall)  # command=Open file method
        fileMenu.add_separator()
        fileMenu.add_command(label="Save")  # command=Save method
        fileMenu.add_command(label="Save As")  # command=Save as method
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit")  # command=Exit method
        self.add_cascade(label="File", menu=fileMenu)

        # Edit Menu
        editMenu = tk.Menu(self, tearoff=0)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        self.add_cascade(label="Edit", menu=editMenu)

        # Run Menu
        runMenu = tk.Menu(self, tearoff=0)
        runMenu.add_command(label="Run")  # command=Run method
        self.add_cascade(label="Run", menu=runMenu)

        # Help menu
        helpMenu = tk.Menu(self, tearoff=0)
        helpMenu.add_command(label="Settings")  # settings window
        self.add_cascade(label="Help", menu=helpMenu)


class StatusBar(tk.Frame):
    """
    Status bar at the bottom to contain information such as 
    current tool and mouse position
    """

    def __init__(self, master, sprites):
        super(StatusBar, self).__init__(master)

        self.images = sprites

        self.config(relief=tk.RAISED)
        # a label to show current tool
        self.toolModeLbl = tk.Label(self, text="Tool:", relief=tk.SUNKEN, bd=1, anchor=tk.W)
        self.toolModeLbl.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # a label to show current mouse coordinates
        self.mouseLbl = tk.Label(self, text="[ , ]", relief=tk.SUNKEN, bd=1, anchor=tk.W)
        self.mouseLbl.pack(side=tk.RIGHT)

        # a label to show a value that changes when you scroll
        self.scrollLbl = tk.Label(self, image=self.images[0], relief=tk.SUNKEN, bd=1, anchor=tk.W)
        self.scrollLbl.pack(side=tk.RIGHT)
        self.currentScroll = 0

        self.pack(side=tk.BOTTOM, fill=tk.X)

    def setMouseLbl(self, event):
        """
        setting the mouse Label
        """
        self.mouseLbl.config(text='[' + str(event.x) + ';' + str(event.y) + ']')
        self.mouseLbl.update_idletasks()

    def setToolModeLbl(self, tool):
        """
        set the tool mode label
        """
        self.toolModeLbl.config(text="Tool: " + tool)
        self.toolModeLbl.update_idletasks()

    def setScrollLbl(self, scrollValue):
        self.scrollLbl.config(image=self.images[scrollValue])
        self.toolModeLbl.update_idletasks()