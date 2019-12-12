#!/usr/bin/python
"""Progress Bar 3

Frameless and no title bar.
Centred in the screen.

Bigger font size.
Bigger width progress bar.
"""

__version__ = "1.0"
__author__ = "simon.peverett@gmail.com"
__all__ = ['__version__', '__author__']

import sys
if (sys.version_info > (3, 0)):
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import Progressbar
else:
    from Tkinter import *
    from tkFont import Font
    from tkk import Progressbar


class FancyProgressBar(object):
    def __init__(self, parent):
        """A fancy progress bar"""
        self.parent = parent

        self.font = Font(family="Consolas", size=36)
        self.value = StringVar()

        self.frm = Frame( parent, bd=5, height=300, width=200, bg="black" )
        self.frm.pack(side=TOP, fill=X, expand=NO)

        self.legend = Label(
                self.frm, text="Downloading virus...", width=30, justify=CENTER,
                padx=5, pady=5, bg="black", fg="green2", font=self.font
                )
        self.legend.pack(side=TOP, fill=X, expand=YES)

        self.pf = Frame( self.frm, bd=20, bg="black")
        self.pf.pack(side=TOP, fill=X, expand=YES)
        self.progress = Progressbar(
                self.pf, orient="horizontal", mode="determinate",
                length=200
                )
        self.progress.pack(side=TOP, fill=X, ipady=25)
        self.progress["maximum"] = 100
        self.value.set( "{} %".format(self.progress["value"]) )
        
        self.pg_text = Label(
                self.frm, textvariable=self.value, width=30, justify=CENTER,
                padx=5, pady=6, bg="black", fg="green2", font=self.font
                )
        self.pg_text.pack(side=TOP, fill=X, expand=NO)

        self.frm.after(100, self.auto_inc)

    def auto_inc(self):
        self.progress.step()
        self.value.set( "{} %".format( int(self.progress["value"])) )
        if self.progress["value"] < 99:
            self.frm.after(100, self.auto_inc)
        else:
            self.progress["value"] = 100
            self.value.set( "Complete." )
            self.frm.after(2000, self.destroy)

    def destroy(self):
        self.parent.destroy()

def centre(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()

    # PyQt way to find the screen resolution
    # app = QtGui.QApplication([])
    # screen_width = app.desktop().screenGeometry().width()
    # screen_height = app.desktop().screenGeometry().height()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2

    toplevel.geometry("+%d+%d" % (x, y))

def main():
    """Main function"""
    root = Tk()
    
    # Tell the window manager this is a splash window, so no border and no
    # title bar.
    root.wm_overrideredirect(True)
    control = FancyProgressBar(root)
    centre(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
    
    

    

