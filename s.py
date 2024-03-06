from tkinter import *
import customtkinter as tk
import tkintermapview as tmv

tk.set_appearance_mode("light")
tk.set_default_color_theme("blue")

app = tk.CTk()
app.geometry("341x584")
app.resizable(False,False)
app.title("ParkOn - TechStack")

top_frame=tk.CTkFrame(master=app,height=74,width=342,fg_color="black",corner_radius=0)
top_frame.grid(row=0,column=0)

top_label=tk.CTkLabel(master=top_frame,text="ParkOn",text_color="white",font=("Helvetica Bold",20))
top_label.grid(row=0,column=0,padx=138,pady=10)

map_widget=tmv.TkinterMapView(app,height=537,width=342)
map_widget.grid(row=1,column=0)

search_button=tk.CTkButton(master=map_widget,text="Search",fg_color="black",text_color="white",font=("Helvetica Bold",20))
search_button.grid(row=0,column=0,sticky='s')

app.mainloop()
