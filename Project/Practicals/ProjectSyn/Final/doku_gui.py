from tkinter import *
from doku import *
from time import sleep
#Root main window and main sudoku variable
tkinterSudoku = [[0 for _ in range(10)] for __ in range(10)]
root = Tk()


#attributes of root window
root.title("Sudoku Solver")
root.geometry('725x700')
root.resizable(False , False)
root.configure(bg="Yellow")
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

#3 chilren of root window
TitleFrame = Frame(root)
MainFrame = Frame(root,bg="black", height=40, padx=1,pady=1)
BottomFrame = Frame(root,bg="Yellow",width = 100, height=40)


#initialise string variable
vival = [[StringVar(root, value=" ") for _ in range(10)] for __ in range(10)]

#Set the values of CornerGrids
for j in range(1,10):
    vival[0][j].set(j)
for j in range(1,10):
    vival[j][0].set(" ABCDEFGHI"[j])


#Function for editing value of Grid - Used for Button
def EditStringVar(a,i,j,val):
    a[int(j)+1][int(i)].set(str(val))
    print(i,int(j)+1)

#Function for converting vival to board
def convertBoard():
    takenBoard = [[int(vival[i][j].get())
    if vival[i][j].get().isnumeric()
    else vival[i][j].get()
    for j in range(1,10)]
    for i in range(1,10)]

    solveBoard(takenBoard)
    print(takenBoard)
    for i in range(9):
        for j in range(9):
            vival[i+1][j+1].set(takenBoard[i][j])
            root.update()
            sleep(0.013)


#Create the sudoku itself by making labels and assigning String Variable
def MakeSudoku(a):
    for i in range(10):
        for j in range(10):
            tkinterSudoku[i][j] = Label(MainFrame, width=4, height=1, bg="white",textvariable=a[i][j],padx=1,pady=1,font=("Comic Sans MS",18)).grid(row=i,column=j,padx=1,pady=2)


def buttonCommand():
    EditStringVar(
            vival,
            int(   option1.get()  ),
            "ABCDEFGHI".index(option2.get()),
            int(   option3.get()  ) )


#Makes Title and the Solve Button

title = Label(TitleFrame, width=24 , height=2 , text="Sudoku Solver",font="Algerian 28",bg='Light green')
solveButton = Button(TitleFrame, bg="orange",text="Solve", width=10 , height=2,font=("Comic Sans MS 20",20), command=convertBoard)



#makes middle part = Sudoku
MakeSudoku(vival)




#Initialises Base variables for Option menu
one2nine = list("123456789")
a2i = list("ABCDEFGHI")
option1=StringVar(root,value="1")
option2=StringVar(root,value="A")
option3=StringVar(root,value="1")


#Creating Option Menu
Opt1 = OptionMenu(BottomFrame,option1,*one2nine)
Opt2 = OptionMenu(BottomFrame,option2,*a2i     )
Opt3 = OptionMenu(BottomFrame,option3,*one2nine)
Opt1.config(width=3,height=2,bg='light blue',font=("Algerian",18))
Opt2.config(width=3,height=2,bg='light blue',font=("Algerian",18))
Opt3.config(width=3,height=2,bg='light blue',font=("Algerian",18))

#Creates button
OptButton = Button(BottomFrame, width=10,height=2,text="Put Value",
            command=buttonCommand,font=("Algerian",18))



Opt1.pack(expand=True,side=LEFT,padx=40,pady=35)
Opt2.pack(expand=True,side=LEFT,padx=40,pady=35)
Opt3.pack(expand=True,side=LEFT,padx=40,pady=35)
OptButton.pack(side=LEFT)

#Makes root's grid
TitleFrame.grid(row=0 , column=0)
MainFrame.grid(row=1 , column=0,pady=20)
BottomFrame.grid(row=2 , column=0)


#make titleframe's grid
title.grid(row=0,column=0)
solveButton.grid(row=0,column=1)


#begins window launch
root.mainloop()
