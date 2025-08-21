from tkinter import *

window = Tk()
window.title("Miles to kilometer Coverter")
window.config(padx=20,pady=20)

def Calculate():
    Input = MilesEntry.get()
    # print(Input,type(Input))
    TypeE = FALSE
    try:
        Input = float(Input)
    except:
        TypeE = True 
    if not TypeE:
            KiloToMiles = (Input*1.6)
            kilometerResult.config(text=f"{ KiloToMiles}")
    else:
        kilometerResult.config(text=f"Invalid Input")

MilesEntry = Entry()
MilesEntry.grid(column=1 , row=0)

LableM = Label(text = "Miles")
LableM.grid(column=2 , row=0)

IsEqual = Label(text = "is equal to")
IsEqual.grid(column=0 , row=1)

kilometerResult = Label(text = 0)
kilometerResult.grid(column=1 , row=1)

kilometerLable = Label(text = "Km")
kilometerLable.grid(column=2 , row=1)

CalculateBtn = Button(text="Calculate" , command =  Calculate)
CalculateBtn.grid(column=1 , row=2)



window.mainloop()

