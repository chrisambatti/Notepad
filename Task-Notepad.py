from tkinter import *
from tkinter import messagebox,filedialog

def main():
    def OpenFile():
        filepath = filedialog.askopenfile('r',defaultextension='txt')
        # print(filepath)
        file = open(filepath.name,filepath.mode,encoding="utf-8")
        # print(file.read())
        t.insert(0.0,file.read())

    def saveFile():
        filepath = filedialog.asksaveasfile(mode="w",defaultextension="txt")
        file = open(filepath.name,"w",encoding="utf-8")
        file.write(t.get(0.0,END))
        file.close()
        pass

    def NewWindow():
        main()

    def NewFile():
        val = messagebox.askyesnocancel("Notepad","Do you want to save the file")
        print(val)
        if val == True:
            saveFile()
            pass
        elif val == False:
            t.delete(0.0,END) 
        
    def CutText(event):
        s1 = t.selection_get()
        s1_index = t.search(s1,0.0,END)
        s1_len = len(s1)
        print(INSERT)
        i2 = float(s1_index)+float("0." + str(len(s1)))
        t.clipboard_clear()
        t.clipboard_append(s1)
        t.delete(s1_index,i2)
        print(s1)
        pass

    def Pastetext(event):
        text = t.clipboard_get()
        i1 = t.index(INSERT)
        t.insert(i1,text)

    def FindText(event):
        t.tag_configure("start", background= "black", foreground= "white")
        def Find():
            val = e1.get()
            val_len = len(val)
            i1 = t.search(val,0.0,END)
            i2 = float(i1)+float(f"0.{val_len}")
            print(i1)
            t.tag_add('start',i1,i2)
            pass
        w1 = Toplevel(win)

        l1 = Label(w1,text="Find")
        l1.pack()
        f1 = Frame(w1)

        e1 = Entry(f1)
        e1.pack(side=LEFT)
        b1 = Button(f1,text="Find",command=Find)
        b1.pack(side=RIGHT)

        f1.pack()
        w1.mainloop()

    def none():
        pass

    def RedoText():
        t.edit_redo()
        pass

    def UndoText():
        t.edit_undo()

    def DeleteText():
        t.delete(0.0,END)



    win = Tk()
    win.geometry("600x420",)


    menubar = Menu(win)
    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="New Window", command=NewWindow)
    filemenu.add_command(label="Open...", command=OpenFile)
    filemenu.add_command(label="Save", command=saveFile)
    filemenu.add_command(label="Save as...", command=none)
    filemenu.add_separator()
    filemenu.add_command(label="Page setup...", command=none)
    filemenu.add_command(label="Print...", command=none)

    editmenu = Menu(menubar,tearoff=0)
    editmenu.add_command(label="Undo",state=DISABLED, command=none)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=CutText) 
    editmenu.add_command(label="Copy", command=none)
    editmenu.add_command(label="Paste", command=Pastetext)
    editmenu.add_command(label="Delete", command=DeleteText)
    editmenu.add_command(label="Undo", command=UndoText)
    editmenu.add_command(label="Redo", command=RedoText)        
    editmenu.add_separator()
    editmenu.add_command(label="Search with bing...", command=none)
    editmenu.add_command(label="Find", command=FindText)
    editmenu.add_command(label="Find next...",state=DISABLED, command=none)
    editmenu.add_command(label="Find Previous...",state=DISABLED, command=none)
    editmenu.add_command(label="Replace", command=none)
    editmenu.add_command(label="Go to",state=DISABLED, command=none)


    formatmenu = Menu(menubar,tearoff=0)
    formatmenu.add_checkbutton(label="Word wrap",)
    formatmenu.add_command(label="Font",command=none)

    viewmenu = Menu(menubar,tearoff=0)
    zoommenu = Menu(viewmenu,tearoff=0)
    viewmenu.add_cascade(label="zoom",menu=zoommenu)
    zoommenu.add_command(label="Zoom in")
    zoommenu.add_command(label="Zoom out")
    viewmenu.add_checkbutton(label="Status Bar")
    zoommenu.add_command(label="Restore Default zoom")

    helpmenu = Menu(menubar,tearoff=0)
    helpmenu.add_command(label="View Help")
    helpmenu.add_command(label="Send Feedback")
    helpmenu.add_separator()
    helpmenu.add_command(label="About Notepad")

    
    menubar.add_cascade(label="File",menu=filemenu)
    menubar.add_cascade(label="Edit",menu=editmenu)
    menubar.add_cascade(label="Format",menu=formatmenu)
    menubar.add_cascade(label="View",menu=viewmenu)
    menubar.add_cascade(label="Help",menu=helpmenu)


    t = Text(win,undo=True,height=100)
    t.pack(fill="both")

    # f = Frame(win)

    # btn = Button(f,text="Get",command=GetText)
    # btn.pack(side=LEFT)
    # f.pack()

    win.bind("<Control-F>",FindText)
    win.bind("<Control-f>",FindText)
    win.bind("<Control-Z>",UndoText)
    win.bind("<Control-z>",UndoText)
    win.bind("<Control-Y>",RedoText)
    win.bind("<Control-y>",RedoText)
    win.bind("<Control-X>",CutText)
    win.bind("<Control-x>",CutText)

    win.config(menu=menubar)
    win.mainloop()

main()