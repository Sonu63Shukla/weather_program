from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=bebe0b90034ee85a6878dbe28d3fc111").json()
    wc_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pres_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("sonu shukla")
win.config(bg="lightblue")
win.geometry("500x570")

name_label = Label(win, text="Weather Forecast", font=("Time New Roman", 35, "bold"))

name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


com = ttk.Combobox(win, text="Weather Forecast", values=list_name, font=("Time New Roman", 15, "bold"), textvariable=city_name)

com.place(x=25, y=120, height=40, width=450)


wc_label = Label(win, text="Weather climate", font=("Time New Roman", 15, "bold"))
wc_label.place(x=25, y=260, height=50, width=200)
wc_label1 = Label(win, text="", font=("Time New Roman", 15, "bold"))
wc_label1.place(x=240, y=260, height=50, width=200)


wd_label = Label(win, text="Weather discription", font=("Time New Roman", 15, "bold"))
wd_label.place(x=25, y=330, height=50, width=200)
wd_label1 = Label(win, text="", font=("Time New Roman", 15, "bold"))
wd_label1.place(x=240, y=330, height=50, width=200)


temp_label = Label(win, text="Temperature", font=("Time New Roman", 20, "bold"))
temp_label.place(x=25, y=400, height=50, width=200)
temp_label1 = Label(win, text="", font=("Time New Roman", 20, "bold"))
temp_label1.place(x=240, y=400, height=50, width=200)


pres_label = Label(win, text="pressure", font=("Time New Roman", 20, "bold"))
pres_label.place(x=25, y=470, height=50, width=200)
pres_label1 = Label(win, text="", font=("Time New Roman", 20, "bold"))
pres_label1.place(x=240, y=470, height=50, width=200)

done_button = Button(win, text="Done", font=("Time New Roman", 15, "bold"), command=data_get)
done_button.place(y = 180, height=40, width=100, x = 200)

win.mainloop()


