from customtkinter import * 


root = CTk()

#hajm nafida
#centering the window
root.geometry("600x400+400+100")
root.title("Custom Tkinter Example learning test")


#root.maxsize(width=700, height=500)

root.minsize(width=800, height=600)
root.resizable(width=False, height=False)

#backgrawnd
root.configure(fg_color='blue')

# the bar color
#root._set_appearance_mode("dark")
#root._set_appearance_mode("light")
root._set_appearance_mode("system")



# icon the app
root.iconbitmap("logo.ico")






#--------frame--------
frame1= CTkFrame(master=root, width=300, height=200, corner_radius=10, fg_color="red", border_width=5, border_color="black")
frame1.place(x=20,y=20)

frame2= CTkFrame(master=root, width=300, height=200, corner_radius=10, fg_color="green", border_width=5, border_color="black")
frame2.place(x=345,y=20)






root.mainloop()