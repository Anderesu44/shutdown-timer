# from client.ui import Panel
from os import system as cmd
from tkinter import messagebox as mb

def label_set(*null,minutes:int|None = None, seconds:int|None = None, mode:int = 0)->str:
    if minutes:
        seconds_ = minutes*60
    elif seconds:
        seconds_ = seconds
        # print(seconds_)
    else :
        raise TypeError(" label_set() missing 1 required keyword-only argument: 'minutes' or 'seconds' ")
    if mode == 0:    
        if seconds_ < 60:
            return_ = f"{seconds_}.sec"
        elif seconds_ >= 60 and seconds_ < 3600:
            return_ = f"{seconds_//60}.min"
        elif seconds_ >= 3600 and seconds_ < 86400:
            return_ = f"{seconds_ // 3600}.h"
        else:
            raise ValueError("actualmente no soportado")
        return return_
    elif mode == 1:
        if seconds_ < 60:
            if seconds_ > 1:
                return_ = f"{seconds_} segundos"
            else:
                return_ = f"{seconds_} segundo"
        elif seconds_ >= 60 and seconds_ < 3600:
            if seconds_ // 60 > 1:
                return_ = f"{seconds_//60} minutos"
            else:
                return_ = f"{seconds_//60} minuto"
        elif seconds_ >= 3600 and seconds_ < 86400:
            if seconds_ // 3600 > 1:
                return_ = f"{seconds_ // 3600} horas"
            else:
                return_ = f"{seconds_ // 3600} hora"
        else:
            raise ValueError("actualmente no soportado")
        return return_

def shutdown(t,s):
    if ((lambda x:1 if x == "yes" else 0)(mb.askquestion("apagado programado", f"¿desea programar el apagado de su equipo en {t}?"))):
        cmd(f"shutdown -s -t {s} -c \"usted programo el apagado de su dispositivo mediante 'just shutdown by A44'\"")

def reset(t,s):
    if ((lambda x:1 if x == "yes" else 0)(mb.askquestion("apagado programado", f"¿desea programar el reinicio de su equipo en {t}?"))):
        cmd(f"shutdown -r -t {s} -c \"usted programo el reinicio de su dispositivo mediante 'just shutdown by A44'\"")

# def keys_funtions(p:Panel,*args,**kwargs):
def keys_funtions(p,*args,**kwargs):
    p.root.bind_all('<Button-1>',p.refres)
    p.root.bind_all('<Up>',p.refres)
    p.root.bind_all('<Down>',p.refres)
    p.root.bind_all('<Left>',p.refres)
    p.root.bind_all('<Right>',p.refres)
    p.root.bind_all('<Control-V>',p.refres)
    p.root.bind_all('<BackSpace>',p.refres)
    p.root.bind_all('<0>',p.refres)
    p.root.bind_all('<9>',p.refres)
    p.root.bind_all('<8>',p.refres)
    p.root.bind_all('<7>',p.refres)
    p.root.bind_all('<6>',p.refres)
    p.root.bind_all('<5>',p.refres)
    p.root.bind_all('<4>',p.refres)
    p.root.bind_all('<3>',p.refres)
    p.root.bind_all('<2>',p.refres)
    p.ui.bind_all('<1>',p.refres)



    