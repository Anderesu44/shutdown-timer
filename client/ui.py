from tkinter import Tk,Frame, StringVar, Button, Label, Entry

class Ui(Frame):
    def __init__(self, root:Tk):
        super().__init__(root)
        self.config(bg=("#334433"))
        self.root = root
        self.pack()

        self.miniscreen_str = StringVar()

        self.ps = 0
        self.pm = 10
        self.ph = 0
        
        self.c = Counter(self)
        self.p = Panel(self)

class Counter(Frame):
    def __init__(self, root:Ui):
        super().__init__(root)
        self.ui = root
        self.root = root.root

        self.pack()
        self.screen_1()
    def screen_1(self,*args,**kwargs):
        bg = "#334433"
        self.config(bg=(bg))

        self.ui.miniscreen_str.set("10.min")#!saca esto cuando ya tengas el "set" configurado
        self.miniscreen = Label(self,textvariable=self.ui.miniscreen_str,bg="#334433",font=("CALIBRI",100))
        self.miniscreen.grid(row=0,column=0,padx=0,pady=10,columnspan=500,rowspan=1)
        
        self.booton_0 = Button(self,width=5,height=1,font=("Arial",15),text="5.min",command=self.set_5)
        self.booton_0.grid(row=1,column=0,rowspan=1,padx=(10,5),pady=5)

        self.booton_1 = Button(self,width=5,height=1,font=("Arial",15),text="10.min",command=self.set_10)
        self.booton_1.grid(row=1,column=100,rowspan=1,padx=5,pady=5)

        self.booton_2 = Button(self,width=5,height=1,font=("Arial",15),text="30.min",command=self.set_30)
        self.booton_2.grid(row=1,column=200,rowspan=1,padx=5,pady=5)

        self.booton_3 = Button(self,width=5,height=1,font=("Arial",15),text="45.min",command=self.set_45)
        self.booton_3.grid(row=1,column=300,rowspan=1,padx=5,pady=5)

        self.booton_4 = Button(self,width=5,height=1,font=("Arial",15),text="1.hour",command=self.set_60)
        self.booton_4.grid(row=1,column=400,rowspan=1,padx=(5,10),pady=5)
    
    def set_5(self,):
        self.ui.miniscreen_str.set(self.root.label_set(minutes=5))
        self.ui.pm = 5
        self.ui.p.set_time(5)
        
    def set_10(self,):
        self.ui.miniscreen_str.set(self.root.label_set(minutes=10))
        self.ui.pm = 10
        self.ui.p.set_time(10)

    def set_30(self,):
        self.ui.miniscreen_str.set(self.root.label_set(minutes=30))
        self.ui.pm = 30
        self.ui.p.set_time(30)

    def set_45(self,):
        self.ui.miniscreen_str.set(self.root.label_set(minutes=45))
        self.ui.pm = 45
        self.ui.p.set_time(45)

    def set_60(self,):
        self.ui.miniscreen_str.set(self.root.label_set(minutes=60))
        self.ui.ph = 1
        self.ui.p.set_time(60)
        self.ui.p.refres()
class Panel(Frame):
    def __init__(self, root:Ui):
        super().__init__(root)
        self.ui = root
        self.root = root.root
        self.pack()
        self.screen_1()
        self.root.keys_funtions(self)
        self.hours.set(0)
        self.min_0.set(1)
        self.min_1.set(0)
        self.seg_0.set(0)
        self.seg_1.set(0)

    def set_time(self,min):
        h = min // 60
        min_0 = (min // 10)
        min_1 = min - min_0 * 10
        seg_0 = 0
        seg_1 = 0
        #set
        self.hours.set(int(h))
        self.min_0.set(int(min_0))
        self.min_1.set(int(min_1))
        self.seg_0.set(int(seg_0))
        self.seg_1.set(int(seg_1))
        #
        self.ui.ps = int(f"{seg_0}{seg_1}")
        self.ui.pm = int(f"{min_0}{min_1}")
        self.ui.ph = h

    def screen_1(self,*args,**kwargs):
        bg = "#334433"
        self.config(bg=(bg))

        #!Colocare todos los entrys y sus respectivos StringsVar arriba para que se pueda navegar mas facil con el tabulador
        #!Estan el mismo orden que antes sus grids se quedan el mismo lugar por si quieres ubicarlos
        
        self.hours = StringVar()
        self.entry_0 = Entry(self,textvariable=self.hours,width=3,justify="center")#?horas

        self.min_0 = StringVar()
        self.entry_1 = Entry(self,textvariable=self.min_0,width=3,justify="center")#?minutos
        self.min_1 = StringVar()
        self.entry_2 = Entry(self,textvariable=self.min_1,width=3,justify="center")#?minutos
        
        self.seg_0 = StringVar()
        self.entry_3 = Entry(self,textvariable=self.seg_0,width=3,justify="center")#?segundos
        self.seg_1 = StringVar()
        self.entry_4 = Entry(self,textvariable=self.seg_1,width=3,justify="center")#?segundos

        #?hora
        self.booton_0 = Button(self,width=2,height=1,font=("Arial",12),text="▲",command=self.h_up,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_0.grid(row=0,column=1,rowspan=1,padx=5,pady=(5,0))

        self.entry_0.grid(row=1,column=1,rowspan=1,padx=0,pady=0)

        self.dot = StringVar(value=":")
        self.label_0 = Entry(self,bg="#334433",font=("ARIAL",15),width=1,textvariable=self.dot,state="disable",borderwidth=0,disabledbackground="#334433",disabledforeground="#000000")
        self.label_0.grid(row=1,column=2,padx=0,pady=0,columnspan=1,rowspan=1)

        self.booton_1 = Button(self,width=1,height=1,font=("Arial",12),text="▼",command=self.h_down,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_1.grid(row=2,column=1,rowspan=1,padx=0,pady=0)

        
        self.label_1 = Label(self,bg="#334433",font=("CALIBRI",0),text="#"*45,fg="#334433")
        self.label_1.grid(row=3,column=0,padx=0,pady=0,columnspan=450,rowspan=1)

        self.label_1 = Label(self,bg="#334433",font=("CALIBRI",0),text="A44",fg="#000000")
        self.label_1.grid(row=3,column=451,padx=0,pady=0,columnspan=50,rowspan=1)


        #?minutos
        self.booton_2 = Button(self,width=2,height=1,font=("Arial",12),text="▲",command=self.min_0_up,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_2.grid(row=0,column=3,rowspan=1,padx=(0,0),pady=(5,0))

        self.booton_3 = Button(self,width=2,height=1,font=("Arial",12),text="▲",command=self.min_1_up,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_3.grid(row=0,column=4,rowspan=1,padx=(0,0),pady=(5,0))

        
        self.entry_1.grid(row=1,column=3,rowspan=1,padx=0,pady=0,columnspan=1)

        self.entry_2.grid(row=1,column=4,rowspan=1,padx=0,pady=0,columnspan=1)

        self.dot = StringVar(value=":")
        self.label_2 = Entry(self,bg="#334433",font=("ARIAL",15),width=1,textvariable=self.dot,state="disable",borderwidth=0,disabledbackground="#334433",disabledforeground="#000000")
        self.label_2.grid(row=1,column=5,padx=0,pady=0,columnspan=1,rowspan=1)

        self.booton_4 = Button(self,width=1,height=1,font=("Arial",12),text="▼",command=self.min_0_down,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_4.grid(row=2,column=3,rowspan=1,padx=(0,0),pady=(5,0))

        self.booton_5 = Button(self,width=2,height=1,font=("Arial",12),text="▼",command=self.min_1_down,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_5.grid(row=2,column=4,rowspan=1,padx=(0,0),pady=(5,0))

        #?segundos
        self.booton_6 = Button(self,width=2,height=1,font=("Arial",12),text="▲",command=self.seg_0_up,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_6.grid(row=0,column=6,rowspan=1,padx=(0,0),pady=(5,0))

        self.booton_7 = Button(self,width=2,height=1,font=("Arial",12),text="▲",command=self.seg_1_up,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_7.grid(row=0,column=7,rowspan=1,padx=(0,0),pady=(5,0))

        self.entry_3.grid(row=1,column=6,rowspan=1,padx=0,pady=0,columnspan=1)

        self.entry_4.grid(row=1,column=7,rowspan=1,padx=0,pady=0,columnspan=1)

        self.booton_8 = Button(self,width=1,height=1,font=("Arial",12),text="▼",command=self.seg_0_down,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_8.grid(row=2,column=6,rowspan=1,padx=(0,0),pady=(5,0))

        self.booton_9 = Button(self,width=2,height=1,font=("Arial",12),text="▼",command=self.seg_1_down,bg=bg,borderwidth=0,activebackground=bg,activeforeground="#333333")
        self.booton_9.grid(row=2,column=7,rowspan=1,padx=(0,0),pady=(5,0))
        #?other buttons
        self.booton_0 = Button(self,width=3,height=1,font=("Arial",15),text=" ",command=self.set_,bg="#26DD36",activebackground="#16CC26")
        self.booton_0.grid(row=1,column=8,rowspan=1,padx=(10,5),pady=0)

        self.booton_0 = Button(self,width=3,height=1,font=("Arial",15),text="⭕",command=self.shutdown)
        self.booton_0.grid(row=1,column=9,rowspan=1,padx=(5,5),pady=0)

        self.booton_0 = Button(self,width=3,height=1,font=("CAMBRIA",15),text="⟲",command=self.reset)
        self.booton_0.grid(row=0,column=10,rowspan=3,padx=(5,10),pady=0)

    def refres(self,*args,**kwargs):
        #Get
        try:
            h = int(self.hours.get())
        except ValueError:
            h = 0
        try:
            min_0 = int(self.min_0.get())
        except ValueError:
            min_0 = 0
        try:
            min_1 = int(self.min_1.get())
        except ValueError:
            min_1 = 0
        try:
            seg_0 = int(self.seg_0.get())
        except ValueError:
            seg_0 = 0
        try:
            seg_1 = int(self.seg_1.get())
        except ValueError:
            seg_1 = 0
        
        if h > 23:
            h = 0
        if h < 0:
            h = 23
        
        if min_0 > 5:
            min_0 = 0
        if min_0 < 0:
            min_0 = 5
        
        if min_1 > 9 or min_0 == 6:
            min_1 = 0
        if min_1 < 0:
            min_1 = 9
        # print(seg_0)
        if seg_0 > 5:
            seg_0 = 0
        if seg_0 < 0:
            seg_0 = 5
        
        if seg_1 > 9 or seg_0 == 6:
            seg_1 = 0
        if seg_1 < 0:
            seg_1 = 9
        #set
        self.hours.set(int(h))
        self.min_0.set(int(min_0))
        self.min_1.set(int(min_1))
        self.seg_0.set(int(seg_0))
        self.seg_1.set(int(seg_1))
        #
        self.ui.ps = int(f"{seg_0}{seg_1}")
        self.ui.pm = int(f"{min_0}{min_1}")
        self.ui.ph = h
        
    def set_(self):
        s = self.ui.ph * 3600 + self.ui.pm * 60 + self.ui.ps
        self.ui.miniscreen_str.set(self.root.label_set(seconds=s))

    def h_up(self):
       self.hours.set((self.ui.ph + 1))
       self.refres()
    def h_down(self):
       self.hours.set((self.ui.ph - 1))
       self.refres()
    
    def min_0_up(self):
       self.min_0.set((int(self.min_0.get()) + 1))
       self.refres()
    def min_1_up(self):
       self.min_1.set((int(self.min_1.get()) + 1))
       self.refres()

    def min_0_down(self):
       self.min_0.set((int(self.min_0.get()) - 1))
       self.refres()
    def min_1_down(self):
       self.min_1.set((int(self.min_1.get()) - 1))
       self.refres()

    def seg_0_up(self):
       self.seg_0.set((int(self.seg_0.get()) + 1))
       self.refres()
    def seg_1_up(self):
       self.seg_1.set((int(self.seg_1.get()) + 1))
       self.refres()

    def seg_0_down(self):
       self.seg_0.set((int(self.seg_0.get()) - 1))
       self.refres()
    def seg_1_down(self):
       self.seg_1.set(int(self.seg_1.get()) - 1)
       self.refres()
    
    def shutdown(self):

        s = self.ui.ph * 3600 + self.ui.pm * 60 + self.ui.ps
        b = "h: " + str(self.ui.ph)
        c = ""
        self.root.shutdown((f"{self.root.label_set(seconds=s,mode=1)}\t({(lambda x : b if x != 0 else c) (self.ui.ph)} min:{self.ui.pm} seg:{self.ui.ps})"),(s))

    def reset(self):

        s = self.ui.ph * 3600 + self.ui.pm * 60 + self.ui.ps
        b = "h: " + str(self.ui.ph)
        c = ""
        self.root.reset((f"{self.root.label_set(seconds=s,mode=1)}\t({(lambda x : b if x != 0 else c) (self.ui.ph)} min:{self.ui.pm} seg:{self.ui.ps})"),(s))

    def set_5(*args,**kwargs):
        pass
    

#*↓↓↓↓⬇|↓↑ꓦꓥ▲►▼◄㋐