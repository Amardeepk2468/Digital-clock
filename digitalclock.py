from tkinter import *
import datetime
def date_time():
    time=datetime.datetime.now()
    hr=time.strftime("%I")
    mi=time.strftime("%M")
    sec=time.strftime("%S")
    am=time.strftime("%p")
    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%y")
    day=time.strftime("%a")
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200,date_time)



clock=Tk()
clock.title("                            ****Digital Clock****"        )
clock.geometry("1000x500")
clock.config(bg="#FF9633")

lab_title=Label(clock,text="Digital Clock",font=("Time New Roman",20,"bold"),bg="red",fg="#ffccff")
lab_title.place(x=380,y=5,height=50,width=180)

lab_hr=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="yellow",fg="white")
lab_hr.place(x=40,y=60,height=100,width=180)

lab_min=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="yellow",fg="white")
lab_min.place(x=260,y=60,height=100,width=180)

lab_sec=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="yellow",fg="white")
lab_sec.place(x=480,y=60,height=100,width=180)

lab_am=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="yellow",fg="white")
lab_am.place(x=700,y=60,height=100,width=180)

lab_hr1=Label(clock,text="Hour",font=("Time New Roman",40,"bold"),bg="yellow",fg="white")
lab_hr1.place(x=40,y=200,height=50,width=180)

lab_min1=Label(clock,text="min",font=("Time New Roman",40,"bold"),bg="yellow",fg="white")
lab_min1.place(x=260,y=200,height=50,width=180)

lab_sec1=Label(clock,text="sec",font=("Time New Roman",40,"bold"),bg="yellow",fg="white")
lab_sec1.place(x=480,y=200,height=50,width=180)

lab_am1=Label(clock,text="am/pm",font=("Time New Roman",40,"bold"),bg="yellow",fg="white")
lab_am1.place(x=700,y=200,height=50,width=180)

lab_date=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="yellow",fg="white")
lab_date.place(x=40,y=280,height=100,width=180)

lab_month=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="yellow",fg="white")
lab_month.place(x=260,y=280,height=100,width=180)

lab_year=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="yellow",fg="white")
lab_year.place(x=480,y=280,height=100,width=180)

lab_day=Label(clock,text="00",font=("Time New Roman",50,"bold"),bg="yellow",fg="white")
lab_day.place(x=700,y=280,height=100,width=180)


lab_date1=Label(clock,text="day",font=("Time New Roman",40,"bold"),bg="yellow",fg="white")
lab_date1.place(x=40,y=420,height=50,width=180)

lab_month1=Label(clock,text="month",font=("Time New Roman",40,"bold"),bg="yellow",fg="white")
lab_month1.place(x=260,y=420,height=50,width=180)

lab_year1=Label(clock,text="year",font=("Time New Roman",40,"bold"),bg="yellow",fg="white")
lab_year1.place(x=480,y=420,height=50,width=180)

lab_day1=Label(clock,text="day",font=("Time New Roman",40,"bold"),bg="yellow",fg="white")
lab_day1.place(x=700,y=420,height=50,width=180)

date_time()

clock.mainloop()