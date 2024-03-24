import tkinter as tk
import ttkbootstrap as ttk
from Market import create_market
from Watchlist import create_watchlist
from Options import create_options, configurations
from dataHandle import cleanDataSingle
from polygon import RESTClient
from polygonAPIkey import polygonAPIkey
import pandas as pd

client = RESTClient(polygonAPIkey)


def search_stock():
    search=entry_search.get()

def profile():
    Name= ""

def back():
    linkedarray=''
    
def forward():
    linkedarray=''

def Market():
    for child in body_win.winfo_children():
        child.destroy()
    create_market(body_win, w, h)
    Market_button.configure(bg = win_color)
    Watchlist_button.configure(bg = top_bar_color)
    Options_Button.configure(bg = top_bar_color)
    
def Watchlist():
    for child in body_win.winfo_children():
        child.destroy()
    create_watchlist(body_win, w, h)
    Market_button.configure(bg = top_bar_color)
    Watchlist_button.configure(bg = win_color)
    Options_Button.configure(bg = top_bar_color)

def Options():
    for child in body_win.winfo_children():
        child.destroy()
    create_options(body_win, w, h)
    Market_button.configure(bg = top_bar_color)
    Watchlist_button.configure(bg = top_bar_color)
    Options_Button.configure(bg = win_color)
    
top_bar_color='grey18'
win_color='grey26'
buttonOn_color='grey30'

display = "Sign In / Sign Up"

window = ttk.Window()
window.configure(background = 'grey28')
window.title('Stock Market App')
window.state('zoomed')
w , h = window.maxsize()

#top bar
top_win = tk.Frame(master = window, width = w, height = h*.118)
top_win.pack_propagate(False)
top_win.configure(bg = top_bar_color)
top_win.pack()

title_label = tk.Label(master = top_win, text = 'Stock Market App', font = "Calibri 20")
title_label.configure(bg = top_bar_color, fg = 'white')

search_button = tk.Button(master = top_win, text = 'Search', font = "Calibri 15", command = search_stock)
search_button.configure(background = win_color, activebackground = buttonOn_color)

entry_search = tk.StringVar()
search_bar = tk.Entry(master = top_win, textvariable = entry_search)

profile_button = tk.Button(master = top_win, text = display, font = "Calibri 12", command = profile)
profile_button.configure(background = top_bar_color, activebackground = buttonOn_color)

back_button = tk.Button(master = top_win, text = '<', font = "Calibri 20", command = back)
back_button.configure(background = top_bar_color, activebackground = buttonOn_color)

forward_button = tk.Button(master = top_win, text = '>', font = "Calibri 20", command = forward)
forward_button.configure(background = top_bar_color, activebackground = buttonOn_color)

Market_button = tk.Button(master = top_win, text = 'Market', font = "Calibri 20", command = Market)
Market_button.configure(background = top_bar_color, activebackground = buttonOn_color)

Watchlist_button = tk.Button(master = top_win, text = 'Watchlist', font = "Calibri 20", command = Watchlist)
Watchlist_button.configure(background = top_bar_color, activebackground = buttonOn_color)

Options_Button = tk.Button(master = top_win, text = 'Options', font = "Calibri 20", command = Options)
Options_Button.configure(background = top_bar_color, activebackground = buttonOn_color)

title_label.place(x = w*.08, y = h*.005)
search_button.place(x = w*.26, y = h*.014, width = w*.065, height = h*.03)
search_bar.place(x = w*.26 + w*.065 , y = h*.014, width = w*.46, height = h*.03)
profile_button.place(x = w*.78, y = h*.014, height = h*.03)

back_button.place(x = w*.008, y = h*.059, width = w*.016)
forward_button.place(x = w*.008 + w*.016 , y = h*.059, width = w*.016)
Market_button.place(x = w*.26, y = h*.059, width = w*.082, height = h*.058)
Watchlist_button.place(x = w*.47, y = h*.059, width = w*.082, height = h*.058)
Options_Button.place(x = w*.69, y = h*.059, width = w*.082, height = h*.058)

#body
body_win = tk.Frame(master = window, width = w, height = h - h*.118)
body_win.pack_propagate(False)
body_win.configure(bg = win_color)
body_win.pack()

#display market in body on startup
create_market(body_win, w, h)

window.mainloop()