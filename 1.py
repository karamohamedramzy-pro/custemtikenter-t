from customtkinter import * 


root = CTk()

#hajm nafida
#centering the window
root.geometry("600x400+400+100")
root.title("Custom Tkinter Example learning test")


#root.maxsize(width=700, height=500)

root.minsize(width=400, height=400)
root.resizable(width=False, height=False)

#backgrawnd
root.configure(fg_color='blue')

# the bar color
#root._set_appearance_mode("dark")
#root._set_appearance_mode("light")
root._set_appearance_mode("system")



# icon the app
root.iconbitmap("logo.ico")


root.mainloop()