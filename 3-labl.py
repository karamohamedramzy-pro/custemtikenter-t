from customtkinter import * 
#import librer img
from PIL import Image
#pip install pillow


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






#--------label--------
lbl= CTkLabel(master=root, text="Hello World",font=('Arial', 16,'bold'), width=200, height=50, corner_radius=10, fg_color="red", border_width=5, border_color="black")
#pack يضع label في منتصف الشاشة
lbl.pack(fill=X)

lbl2= CTkLabel(master=root, text="user name",text_color='blue',font=('Arial', 14,'bold'), width=200, height=50, corner_radius=10, fg_color="green", border_width=5, border_color="black")
lbl2.place(x=20,y=100)



#=========img


photo = CTkImage(light_image=Image.open("tb-icon-and-logo-vector.jpg"), size=(100, 100))
lbl3= CTkLabel(master=root, text="TB image oki",
               text_color='blue',
               font=('Arial', 14,'bold'),
                 width=250,
                height=150, corner_radius=10,
                  fg_color="green",
                    border_width=5,
                      border_color="black",
                        image=photo,
                        compound="bottom" # top / bottom / left / right
                        )

lbl3.place(x=20,y=200)

root.mainloop()
