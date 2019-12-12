#!/usr/bin/python
"""
Frameless and no title bar.
Centred in the screen.

Really big text. 2nd line flashes a defined number of times.
"""

__version__ = "1.0"
__author__ = "simon.peverett@gmail.com"
__all__ = ['__version__', '__author__']

from tkinter.font import Font
from tkinter import *
from tkinter.ttk import Progressbar
import sys
#    from tkinter import messagebox, filedialog

class AccessDenied(object):
    def __init__(self, parent, line1="ACCESS", color1="green2", line2="DENIED", color2="red", repeat=7):
        """Access Denied"""
        self.parent = parent
        self.repeat = repeat
        self.line1 = line1
        self.line2 = line2
        self.color1 = color1
        self.color2 = color2

        self.font = Font(family="consolas", size=44, weight="bold")
        self.value = StringVar()

        self.frm = Frame( parent, bd=5, height=300, width=200, bg="black" )
        self.frm.pack(side=TOP, fill=X, expand=NO)

        self.legend = Label(
                self.frm, text=self.line1, width=10, justify=CENTER,
                padx=5, pady=5, bg="black", fg=self.color1, font=self.font
                )
        self.legend.pack(side=TOP, fill=X, expand=YES)

        self.value.set( "" )
        
        self.pg_text = Label(
                self.frm, textvariable=self.value, width=10, justify=CENTER,
                padx=5, pady=6, bg="black", fg=self.color2, font=self.font
                )
        self.pg_text.pack(side=TOP, fill=X, expand=NO)

        self.frm.after(500, self.auto)

    def auto(self):
        if self.repeat % 2:
            self.value.set( self.line2 )
        else:
            self.value.set( " " )

        self.repeat -= 1
        if self.repeat:
            self.frm.after(500, self.auto)
        else:
            self.frm.after(500, self.destroy)

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
    if len(sys.argv) < 2:
        control = AccessDenied(root)
    else:
        control = AccessDenied(root, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]))
    centre(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
    
