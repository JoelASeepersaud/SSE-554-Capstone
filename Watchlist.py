import tkinter as tk
from tkinter import ttk as ttk2
import ttkbootstrap as ttk

#create watchlist display
def create_watchlist(parent, width, height):
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
    
    top_frame = tk.Frame(master = parent, width = w, height = h*.02)
    top_frame.configure(bg = win_color)
    top_frame.pack()
    
    watchlist_title = tk.Label(master = top_frame, text = 'My Watchlist', font = "Calibri 30")
    watchlist_title.configure(bg = win_color, fg = 'white')
    watchlist_title.pack_propagate(False)
    watchlist_title.pack(pady = (h-h*.118)*.025)
    
    info_frame = tk.Frame(master = parent, width = w*.87)
    info_frame.configure(bg = win_color)
    info_frame.rowconfigure(0, weight = 1)
    info_frame.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform = 'a')
    info_frame.pack(expand = True, fill = 'both', padx = w*.065)
    
    name_text = tk.Label(master = info_frame, text = 'Name', font = "Calibri 15")
    name_text.configure(bg = win_color, fg = 'white')
    name_text.grid(row = 0, column = 0, columnspan = 4, sticky = 'w')
    
    price_text = tk.Label(master = info_frame, text = 'Price', font = "Calibri 15")
    price_text.configure(bg = win_color, fg = 'white')
    price_text.grid(row = 0, column = 4, sticky = 'e')
    
    change_text = tk.Label(master = info_frame, text = 'Change', font = "Calibri 15")
    change_text.configure(bg = win_color, fg = 'white')
    change_text.grid(row = 0, column = 5, sticky = 'e')
    
    changepercent_text = tk.Label(master = info_frame, text = 'Change %', font = "Calibri 15")
    changepercent_text.configure(bg = win_color, fg = 'white')
    changepercent_text.grid(row = 0, column = 6, sticky = 'e')
    
    date_text = tk.Label(master = info_frame, text = 'Date', font = "Calibri 15")
    date_text.configure(bg = win_color, fg = 'white')
    date_text.grid(row = 0, column = 7, sticky = 'e')
    
    divider_frame = tk.Frame(master = parent, width = w*.87, height = 4)
    divider_frame.configure(bg = top_bar_color)
    divider_frame.pack(expand = True, fill = 'x', padx = w*.065)
    
    bot_frame = tk.Frame(master = parent, width = w, height = (h-h*.118)*.83)
    bot_frame.pack_propagate(False)
    bot_frame.pack(side = 'bottom')
    
    text_list = [('1 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024'), ('6 S&P500', '2', '1', '50%', '5/2/2024'), ('7 S&P500', '2', '1', '50%', '5/2/2024'), ('8 S&P500', '2', '1', '50%', '5/2/2024'), ('9 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024'), ('6 S&P500', '2', '1', '50%', '5/2/2024'), ('7 S&P500', '2', '1', '50%', '5/2/2024'), ('8 S&P500', '2', '1', '50%', '5/2/2024'), ('9 S&P500', '2', '1', '50%', '5/2/2024')]
    list_frame = ListFrame(bot_frame, text_list, 70)
    
#create scrollable list
class ListFrame(tk.Frame):
    
    #initialize frame
    def __init__(self, parent, text_data, item_height):
        super().__init__(master = parent)
        self.pack(expand = True, fill = 'both')
        
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height
        
        self.canvas = tk.Canvas(self, scrollregion = (0,0,w,self.list_height))
        self.canvas.configure(bg = win_color)
        self.canvas.pack(expand = True, fill = 'both')
        
        self.frame = tk.Frame(self)
        self.frame.configure(bg = win_color)
        
        for index, item in enumerate(self.text_data):
            created_item=self.create_item(index, item)
            created_item.configure(bg = win_color)
            created_item.pack(expand =True, fill = 'both', pady=4, padx = w*.065)
            created_line = self.create_line()
            created_line.pack(expand =True, fill = 'x', padx = w*.065)
        
        #scrollbar
        self.scrollbar=tk.Scrollbar(self, orient = 'vertical', command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.place(relx=1, rely=0, relheight = 1, anchor = 'ne')
        
        
        #events
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta/60), "units"))
        self.bind('<Configure>', self.update_size)
    
    #get height and determine if scrollable is necessary
    def update_size(self, event):
        if self.list_height >= (h-h*.118)*.67:
            height = self.list_height
            self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta/60), "units"))
            self.scrollbar.place(relx=1, rely=0, relheight = 1, anchor = 'ne')
        else:
            height = (h-h*.118)*.67
            self.canvas.unbind_all('<MouseWheel>')
            self.scrollbar.place_forget()
        self.canvas.create_window((0,0), window = self.frame, anchor = 'nw', width = w, height = height)
        
    #create item row from list 
    def create_item(self, index, item):
        frame = tk.Frame(self.frame)
        
        frame.rowconfigure(0, weight = 1)
        frame.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform = 'a')
        
        name_button=tk.Button(frame, text = f'{item[0]}', font = "Calibri 15")
        name_button.configure(bg = win_color, activebackground = buttonOn_color, fg = 'white')
        name_button.grid(row = 0, column = 0, columnspan = 4, sticky = 'w')
        
        Price_text=tk.Label(frame, text = f'{item[1]}', font = "Calibri 15")
        Price_text.configure(bg = win_color, fg = 'white')
        Price_text.grid(row = 0, column = 4, sticky = 'e')
        
        Change_text=tk.Label(frame, text = f'{item[2]}', font = "Calibri 15")
        Change_text.configure(bg = win_color, fg = 'white')
        Change_text.grid(row = 0, column = 5, sticky = 'e')
        
        Changepercent_text = tk.Label(frame, text = f'{item[3]}', font = "Calibri 15")
        Changepercent_text.configure(bg = win_color, fg = 'white')
        Changepercent_text.grid(row = 0, column = 6, sticky = 'e')

        date_text=tk.Label(frame, text = f'{item[4]}', font = "Calibri 15")
        date_text.configure(bg = win_color, fg = 'white')
        date_text.grid(row = 0, column = 7, sticky = 'e')
        
        return frame
    
    def create_line(self):
        frame = tk.Frame(self.frame, height = 2)
        frame.configure(bg=top_bar_color)
        
        return frame
