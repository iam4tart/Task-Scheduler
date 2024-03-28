from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from PIL import ImageTk, Image
from PIL import ImageDraw
import dbfile as db
import edit_notes as edit_notes
import main_menu as main_menu

class ScrollableFrame(Frame):
    
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self, width = 450, height=515, bg='#FEF4E8', highlightbackground='#FEF4E8', relief='ridge')
        
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        
        def scroll_vertical(event):
            if scrollbar.get() != (0.0, 1.0):
                canvas.yview_scroll(-1 * int(event.delta / 60), "units")
                
        def bound_to_mousewheel(event):
    

            canvas.bind_all('<MouseWheel>', scroll_vertical)

        def unbound_to_mousewheel(event):
    
            canvas.unbind_all('<MouseWheel>')
            

            canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

            canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        canvas.bind("<Enter>", bound_to_mousewheel)
        canvas.bind("<Leave>", unbound_to_mousewheel)
        

   
def update_plan():
   print("Update-Plan")
   
   
class show_notes(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        def headBack():
            self.destroy()
            print("New-Plan")
            
            root = main_menu.main_menu()
            root.state('zoomed')
            root.mainloop()
            
        
        def addNote():
         self.destroy()
         print("Add-Notes")
         
         root = edit_notes.edit_notes()
         root.state('zoomed')
         root.mainloop()
        
        # General Properties
        self.title('Task Scheduler')
        self.geometry('480x900')
        self.minsize(480,900)
        self.maxsize(480,900)
        self['background'] = '#FEF4E8'
        
        # Header
        self.frame_wave = Frame(self, width=400, height=400, bg='#FEF4E8')
        self.frame_wave.place(anchor='center', relx=0.5, rely=0.1)
        self.wave = ImageTk.PhotoImage(Image.open("assets/ShowNotes/notes_header.png")) 
        
        # Back
        self.frame_back = Frame(self, width=400, height=400, bg='#FEF4E8')
        self.frame_back.place(anchor='center', relx=0.08, rely=0.125)
        self.back = ImageTk.PhotoImage(Image.open("assets/Navigation/back.png")) 
        
        # Add a Note
        self.frame_newnote = Frame(self, width=200, height=400, bg='#FEF4E8')
        self.frame_newnote.place(anchor='center', relx=0.5, rely=0.25)
        self.newnote = ImageTk.PhotoImage(Image.open("assets/ShowNotes/add_note.png")) 
        
        # Base
        self.frame_base = Frame(self, width=200, height=400, bg='#FEF4E8')
        self.frame_base.place(anchor='center', relx=0.5, rely=0.33)
        self.base = ImageTk.PhotoImage(Image.open("assets\Intro\iphone_base.png"))
        
        # Show Notes
        self.frame = ScrollableFrame(self)
        self.frame.place(anchor='center', relx=0.5, rely=0.64)
        self.img = ImageTk.PhotoImage(Image.open('assets/ShowNotes/note_container.png'))
        
        #  All added notes
        self.data_dir = []
        self.var = (db.show_notes())
        for i in range(len(self.var)):
            self.data_dir.append([self.var[i]['title'],self.var[i]['description']])
            
        for data in self.data_dir:
            print(data[0])

            self.rise = Canvas(self.frame.scrollable_frame, bg='#FEF4E8', width = 450, height=320, borderwidth=0)
            self.rise.create_image(450,5, anchor=NE, image=self.img)
            self.rise.pack()
   
            self.block_title = Label(self.rise ,bg='#FEF4E8', text = f"{data[0]}",font=("Arial", 18))
            self.rise.create_window(225 , 45, anchor=CENTER, window=self.block_title)
            self.block_desc = st.ScrolledText(self.rise ,bg='white',font=("Arial", 10), width=50, height=12, wrap=WORD, borderwidth=0)
            self.rise.create_window(42 , 85, anchor=NW, window=self.block_desc)
   
            self.block_desc.insert(END, f"{data[1]}")
            self.block_desc.config(state=DISABLED)

        
        self.header = Label(self.frame_wave, image = self.wave, bg='#FEF4E8')
        self.header.grid(row=1,column=1)
        
        self.head_back = Button(self.frame_back, image = self.back, bg='#FEF4E8', borderwidth=0, command=headBack)
        self.head_back.grid(row=1,column=1)

        self.adder = Button(self.frame_newnote, image = self.newnote, bg='#FEF4E8', command = addNote, borderwidth=0)
        self.adder.grid(row=2,column=1) 


        self.sep = Label(self.frame_base, image =self.base, bg='#FEF4E8')
        self.sep.grid(row=4,column=1) 
        

# if __name__ == "__main__":
#     root = show_notes()
#     root.state('zoomed')
#     root.mainloop()