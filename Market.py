import tkinter as tk
import ttkbootstrap as ttk
from DataStore import alphBST, openBST, closeBST, percentBST, volumeBST, watchListStack, searchStock

#create market display
def create_market(parent, width, height, search = None):
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
    
    #sorting options
    sorting_frame = tk.Frame(master = parent, width = w, height = h*.17)
    sorting_frame.configure(bg = win_color)
    sorting_frame.pack()
    
    orderby_text = tk.Label(master = sorting_frame, text = 'Order By:', font = "Calibri 15")
    orderby_text.configure(bg = win_color, fg = 'white')
    
    name_button = tk.Button(master = sorting_frame, text = 'Name', font = "Calibri 15")
    
                          
    open_price_button = tk.Button(master = sorting_frame, text = 'Open Price', font = "Calibri 15")
    
    close_price_button = tk.Button(master = sorting_frame, text = 'Close Price', font = "Calibri 15")
    
    percent_change_button = tk.Button(master = sorting_frame, text = '% Change', font = "Calibri 15")    

    volume_button = tk.Button(master = sorting_frame, text = 'Volume', font = "Calibri 15")    
      
    orderby_text.place              (x = w*.09, y = h*.08)
    name_button.place               (x = w*.18, y = h*.07, width = w*.082, height = h*.058)
    open_price_button.place         (x = w*.18+w*.082-1, y = h*.07, width = w*.082, height = h*.058)
    close_price_button.place        (x = w*.18+w*.082*2-2, y = h*.07, width = w*.082, height = h*.058)
    percent_change_button.place     (x = w*.18+w*.082*3-4, y = h*.07, width = w*.082, height = h*.058)
    volume_button.place             (x = w*.18+w*.082*4-5, y = h*.07, width = w*.082, height = h*.058)
    
    #display information for stock list
    info_frame = tk.Frame(master = parent, width = w*.87)
    info_frame.configure(bg = win_color)
    info_frame.rowconfigure(0, weight = 1)
    info_frame.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform = 'a')
    info_frame.pack(expand = True, fill = 'both', padx = w*.065)
    
    name_text = tk.Label(master = info_frame, text = 'Name', font = "Calibri 15")
    name_text.configure(bg = win_color, fg = 'white')
    name_text.grid(row = 0, column = 0, columnspan = 4, sticky = 'w')
    
    open_price_text = tk.Label(master = info_frame, text = 'Open Price', font = "Calibri 15")
    open_price_text.configure(bg = win_color, fg = 'white')
    open_price_text.grid(row = 0, column = 4, sticky = 'e')
    
    close_price_text = tk.Label(master = info_frame, text = 'Close Price', font = "Calibri 15")
    close_price_text.configure(bg = win_color, fg = 'white')
    close_price_text.grid(row = 0, column = 5, sticky = 'e')
    
    percent_change_text = tk.Label(master = info_frame, text = 'Percent Change', font = "Calibri 15")
    percent_change_text.configure(bg = win_color, fg = 'white')
    percent_change_text.grid(row = 0, column = 6, sticky = 'e')
    
    volume_text = tk.Label(master = info_frame, text = 'Volume', font = "Calibri 15")
    volume_text.configure(bg = win_color, fg = 'white')
    volume_text.grid(row = 0, column = 7, sticky = 'e')
    
    divider_frame = tk.Frame(master = parent, width = w*.87, height = 4)
    divider_frame.configure(bg = top_bar_color)
    divider_frame.pack(expand = True, fill = 'x', padx = w*.065)
    
    #display list of stock
    display_frame = tk.Frame(master = parent, width = w, height = (h-h*.118)*.67)
    display_frame.configure(bg = win_color)
    display_frame.pack_propagate(False)
    display_frame.pack(side = 'bottom')
    
    text_list = list()
    
    if search != None:
        item=searchStock[search]
        if item != None:
            text_list.append(item.nodeHandle())
            list_frame = ListFrame(display_frame, text_list, 70)
        else:
            noItem_text=tk.Label(master = display_frame, text = 'Stock Not Found', font = "Calibri 30")
            noItem_text.configure(bg = win_color, fg = 'white')
            noItem_text.pack()
    else:
        for item in alphBST.inorderTrav():
            text_list.append(item.nodeHandle())
        list_frame = ListFrame(display_frame, text_list, 70)

    name_button.configure           (bg = win_color, 
                                    activebackground = buttonOn_color, 
                                    borderwidth=1, 
                                    relief ='solid', 
                                    command = lambda: list_frame.updateData(text_list, 'Name')
                                    )
    open_price_button.configure     (bg = win_color, 
                                    activebackground = buttonOn_color, 
                                    borderwidth=1, 
                                    relief ='solid',  
                                    command = lambda: list_frame.updateData(text_list, 'OpenPrice')
                                    )

    close_price_button.configure     (bg = win_color,   
                                     activebackground = buttonOn_color, 
                                     borderwidth=1, 
                                     relief ='solid',
                                     command = lambda: list_frame.updateData(text_list, 'ClosePrice')
                                    )

    percent_change_button.configure (bg = win_color,    
                                    activebackground = buttonOn_color, 
                                    borderwidth=1, 
                                    relief ='solid',
                                    command = lambda: list_frame.updateData(text_list, 'PercentChange')
                                    )
    
    volume_button.configure         (bg = win_color, 
                                    activebackground = buttonOn_color, 
                                    borderwidth=1, 
                                    relief ='solid',
                                    command = lambda: list_frame.updateData(text_list, 'Volume')
                                    )
    
#create scrollable list
class ListFrame(tk.Frame):
    
    #initialize frame
    def __init__(self, parent, text_data, item_height):
        super().__init__(master = parent)
        self.pack(expand = True, fill = 'both')

        self.parent = parent
        self.text_data = text_data
        self.item_height = item_height

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
        name_button.configure(bg = win_color, activebackground = buttonOn_color, fg = 'white', command = lambda item = item: watchListStack.push(item))
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
    
    def updateData(self, text_list, sortType):
        for widget in self.frame.winfo_children():
            widget.destroy()

        if sortType == 'Name':
            text_list = list()
            for item in alphBST.inorderTrav():
                text_list.append(item.nodeHandle())
        
        elif sortType == 'OpenPrice':
            text_list = list()
            for item in openBST.inorderTrav():
                text_list.append(item.nodeHandle())
        
        elif sortType == 'ClosePrice':
            text_list = list()
            for item in closeBST.inorderTrav():
                text_list.append(item.nodeHandle())

        elif sortType == 'PercentChange':
            text_list = list()
            for item in percentBST.inorderTrav():
                text_list.append(item.nodeHandle())

        elif sortType == 'Volume':
            text_list = list()
            for item in volumeBST.inorderTrav():
                text_list.append(item.nodeHandle())

        else: raise TypeError("Not a vaild sort type")

        for index, item in enumerate(self.text_data):
            created_item=self.create_item(index, item)
            created_item.configure(bg = win_color)
            created_item.pack(expand =True, fill = 'both', pady=4, padx = w*.065)
            created_line = self.create_line()
            created_line.pack(expand =True, fill = 'x', padx = w*.065)

        self.text_data = text_list
        self.item_number = len(text_list)
        self.list_height = self.item_number * self.item_height
        self.canvas.configure(scrollregion=(0, 0, w, self.list_height))
        self.update_size(None)