__author__ = "A44"
__version__ = "0.1.0"
from client.ui import Ui
from client.ui_functions import label_set,keys_funtions,shutdown,reset


from sys import exit
import tkinter as tk

def main(*args,**kwargs):
    # shutdown("5 horas",18000)
    # exit()
    root = tk.Tk()
    root.config(bg="#334433")
    root.resizable(0,0)
    root.iconbitmap("res\icon.ico")
    root.title("just shutdown")


    root.shutdown = shutdown
    root.reset = reset
    root.label_set = label_set
    root.keys_funtions = keys_funtions


    ui = Ui(root)
    ui.mainloop()


#shutdown -s -t {s} -c "usted programo el apagado de su dispositivo mediante 'erasy shutdown by A44'"
#shutdown -r -t {s} "usted programo el reinicio de su dispositivo mediante 'erasy shutdown by A44'"


if __name__ == '__main__':
    main()