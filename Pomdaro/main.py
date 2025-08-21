from tkinter import *
import math
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Reps = 0
Mark=''
Timer = None



# ---------------------------- TIMER RESET ------------------------------- # 

def ResetTimer():
    global Timer
    global Reps
    Reps=0
    window.after_cancel(Timer)
    canvas.itemconfig(TimerText, text="00:00")
    TitleLable.config(text="Timer")
    CheckMark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def StartTimer():
         global Reps
         Reps += 1
         if Reps%8 ==0:
            # Reps=0
            WorkSec = LONG_BREAK_MIN*60
            TitleLable.config(text="Break",fg=RED)
         elif Reps %2 ==0:
            WorkSec = SHORT_BREAK_MIN * 60
            TitleLable.config(text="Break",fg=PINK)
         else:
            WorkSec = WORK_MIN*60 
            TitleLable.config(text="Timer", fg=GREEN)
         UpdateTimer(WorkSec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def UpdateTimer(count):
    global Reps
    global Mark
    global Timer
    CountMin = math.floor(count/ 60)
    CountSec = count % 60
    if CountMin< 10:
        CountMin=f"0{CountMin}"
    if CountSec < 10:
        CountSec=f"0{CountSec}"
    canvas.itemconfigure(TimerText,text =f"{CountMin}:{CountSec}")
    if count> 0:
        Timer = window.after(1000,UpdateTimer, count-1)
    else:
        StartTimer()
        if Reps%2 ==0:
             Mark+="✔" 
             print(Mark)
             CheckMark.config(text=Mark)
      
        
    




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


TitleLable = Label(text="Timer", fg=GREEN,font=(FONT_NAME,50) ,bg=YELLOW)
TitleLable.grid(column=1,row=0)

canvas = Canvas(width= 200 ,height=224,bg=YELLOW,highlightthickness=0)
File_Path = filePath = os.path.join(os.path.dirname(__file__), "tomato.png")
TomatoImage=PhotoImage(file=File_Path)
canvas.create_image(100,112 ,image=TomatoImage)
TimerText =   canvas.create_text(100,130, text= "00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

StartBtn = Button(text="Start" ,highlightthickness=0, command=StartTimer)
StartBtn.grid(column=0,row=2)

ResetBtn = Button(text= "Reset", highlightthickness=0,command=ResetTimer)
ResetBtn.grid(column=2,row=2)

CheckMark = Label( fg=GREEN,bg=YELLOW ,font=(FONT_NAME,25,"bold"))
CheckMark.grid(column=1,row=3)




window.mainloop()