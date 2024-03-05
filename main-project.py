from tkinter import *
from tkinter import messagebox
windows=Tk()
windows.title("made by amirho3ein")
windows.geometry("300x400")

#کلاس ها
class Time:
    pass
t1=Time()

#تابغ ها
def validate_integer(new_value):
    if new_value.isdigit() or (new_value != "" and new_value[0] == "-" and new_value[1:].isdigit()):
        return True
    else:
        return False
validate_input = windows.register(validate_integer)
def action():
    user_input = input.get()
    if user_input.isdigit() or (user_input != "" and user_input[0] == "-" and user_input[1:].isdigit()):
        seconds=int(input.get())
        # hour converter
        t1.hours=0
        if(seconds>3600):
            t1.hours=seconds//3600
        t1.minutes=0
        # minutes converter
        if(seconds-(t1.hours*3600)>60):
            t1.minutes=((seconds-(t1.hours*3600))//60)
        t1.seconds=seconds-((t1.hours*3600)+(t1.minutes*60))
        x="{0}:{1}:{2}".format(t1.hours,t1.minutes,t1.seconds)
        answer.config(text=":جواب شما میشه\n\n{0}".format(x))
    else:
        messagebox.showerror("خطا", "لطفاً یک عدد صحیح وارد کنید.")
        
def exit():
    result=messagebox.askquestion("خروج","آیا مطمئن هستید که می‌خواهید از برنامه خارج شوید؟")
    if result=="yes":
        windows.quit()
    else:
        pass
        
        
# فریم سازی
frame_1=LabelFrame(windows,text="Input",font="zar",fg="#F6B17A",bg="#2D3250")
frame_1.pack(fill="both",expand=True,side="top")
frame_2=LabelFrame(windows,text="Output",font="zar",fg="#F6B17A",bg="#2D3250")
frame_2.pack(fill="both",expand=True)
# لیبل ها
Label(frame_1,text=":عدد خود را وارد کنید",font=("Ahang BlackSharp",15),
      bg="#2D3250",fg="white").pack(pady=(70,1))

answer=Label(frame_2,text='',font=("Ahang BlackSharp",15),
             bg="#2D3250",fg="white")
answer.pack(side="top")

#ورودی ها
input=Entry(frame_1,bg="white",fg="black",font="tomaha",
            validate="focusout", validatecommand=(validate_input, "%P"))
input.pack(side="left",padx=(30,5))

#دکمه ها
Button(frame_1,text="محاسبه",font=("Ahang BlackSharp",8),
       command=lambda: (action()),
       bg="#F6B17A"
       ).pack(side="left")
Button(frame_2,
       text="خروج",font=("Ahang BlackSharp",10),
       command=lambda: (exit()),
       bg="#F6B17A").pack(side="bottom",anchor="se")
# ساخت منو
menubar=Menu(windows)
filemenubar=Menu(menubar,tearoff=0)
filemenubar.add_command(label="save")
filemenubar.add_command(label="open")
filemenubar.add_command(label="exit",command=windows.quit())
menubar.add_cascade(label="File",menu=filemenubar)

windows.config(menu=menubar)
windows.mainloop()