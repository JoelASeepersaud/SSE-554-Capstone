import tkinter as tk
import ttkbootstrap as ttk
from Configurations import getConfigurations, setConfigurations


#create options display
def create_options(parent, width, height):
    

    global top_bar_color
    global win_color
    global buttonOn_color
    global w
    global h
    top_bar_color='grey18'
    win_color='grey26'
    buttonOn_color='grey30'
    
    w = width
    h = height
    #text=tk.Label(master = parent, text='testing options')
    #text.pack()
    option_frame = tk.Frame(master = parent, width = w*.87)
    option_frame.configure(bg = win_color)
    option_frame.rowconfigure(0, weight = 1)
    option_frame.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform = 'a')
    option_frame.pack(expand = True, fill = 'both', padx = w*.065)

    date_from_frame = OptionFrame(option_frame, 'Date', 'date', getConfigurations())
    option_row = OptionRow(option_frame, date_from_frame)
    option_row.create_line()
    option_row.rowconfigure(0, weight = 1)

class OptionRow(tk.Frame):
    def __init__(self, parent, option_frame):
        super().__init__(master = parent)
        self.configure(bg = win_color)  
        option_frame.pack(expand = True, fill = 'both', padx = w*.065)

    def create_line(self):
        frame = tk.Frame(self, height = 2)
        frame.configure(bg=top_bar_color)
        frame.pack(fill = 'both')

class OptionFrame(tk.Frame):

    #init
    def __init__(self, parent, setting_name, setting, configurations):
        self.setting = setting
        super().__init__(master = parent)
        self.configure(bg = win_color)
        
        self.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight = 1, uniform = 'a')
        self.pack(expand = True, fill = 'both')

        name_frame = tk.Label(master = self, text = setting_name, font = "Calibri 15")
        name_frame.configure(bg = win_color, fg = 'white')
        name_frame.grid(row = 0, column = 3, columnspan = 2, sticky = 'w')

        self.setting_value = tk.StringVar()
        entry_setting = tk.Entry(master = self, textvariable = self.setting_value, font = "Calibri 15")
        entry_setting.configure(bg = win_color, fg = 'white')
        entry_setting.grid(row = 0, column = 5, columnspan = 2, sticky = 'w')

        submit_button = tk.Button(master = self, text = 'Submit', command = lambda :  self.submit_date())
        submit_button.configure(bg = win_color, font = "Calibri 15", activebackground = buttonOn_color, borderwidth=1, relief ='solid')
        submit_button.grid(row = 0, column = 7, columnspan = 2, sticky = 'w')

    def submit_date(self):
        setConfigurations(self.setting, self.setting_value.get())

