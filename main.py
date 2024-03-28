from tkinter import *
import data_caller as dc
import intro_screen as intro_screen
import main_menu as main_menu

def submit_callback(name):
    print("Name --", name.get())
    file = open("your_name.txt", 'w') # writing mode opened
    file.write(name.get()[:15]) # let only name's 15 character allowed
    file.flush()
    file.close()
    root.destroy()
    print("Getting-Started")
    if __name__ == "__main__":
        self = intro_screen.intro_screen()
        self.state('zoomed')
        self.mainloop()
        
def looper():  
    
    root.title("Task Scheduler -- Personalize")
    size = [170,80]
    root.geometry(f"{size[0]}x{size[1]}")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center') # centerize the window

    name_var = StringVar()
    inname_label = Label(root, text = 'Please enter your name:', font=('calibre',10, 'bold'))
    inname_entry = Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    sub_btn = Button(root,text = 'Submit', command = lambda t=name_var: submit_callback(t))
    
    inname_label.grid(row=0,column=0)
    inname_entry.grid(row=2,column=0)
    sub_btn.grid(row=3,column=0)

    root.mainloop()
    
text = dc.get_name()

if len(text) != 0:
     if __name__ == "__main__":
        self = main_menu.main_menu()
        self.state('zoomed')
        self.mainloop()
else:
    root = Tk()
    looper()