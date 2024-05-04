import tkinter as tk
import ttkbootstrap as ttk
from Market import create_market
from Watchlist import create_watchlist
from Options import create_options
from Correlation import create_correlations
from polygon import RESTClient
from DataStructures.Configurations import getPolygonAPIkey
import pandas as pd
from DataStructures import LinkedList

client = RESTClient(getPolygonAPIkey())

#LinkedList for forward/backward buttons
track_action = LinkedList.DoubleLinkedList()
action_index = -1

#search stock
def search_stock():
    search=entry_search.get()
    addMarket(search)

#signin/signup, not implemented
def profile():
    Name= ""

#go to previous page
def back():
    global action_index
    if action_index != 0:
        action_index -= 1
        track_action.getItem(action_index)()
    
#go to next page
def forward():
    global action_index
    if action_index+2 <= track_action.size:
        action_index += 1
        track_action.getItem(action_index)()
      
#load Market and add to LinkedList
def addMarket(search = None):
    global action_index
    action_index += 1
    track_action.insert(Market, action_index)
    Market(search)

#load Market    
def Market(search = None):
    for child in body_win.winfo_children():
        child.destroy()
    create_market(body_win, w, h, search)
    Market_button.configure(bg = win_color)
    Watchlist_button.configure(bg = top_bar_color)
    Options_Button.configure(bg = top_bar_color)
    Correlations_Button.configure(bg = top_bar_color)

#load Watchlist and add to LinkedList
def addWatchlist():
    global action_index
    action_index += 1
    track_action.insert(Watchlist, action_index)
    Watchlist()

#load Watchlist
def Watchlist():
    for child in body_win.winfo_children():
        child.destroy()
    create_watchlist(body_win, w, h)
    Market_button.configure(bg = top_bar_color)
    Watchlist_button.configure(bg = win_color)
    Options_Button.configure(bg = top_bar_color)
    Correlations_Button.configure(bg = top_bar_color)
    
#load Options and add to LinkedList
def addOptions():
    global action_index
    action_index += 1
    track_action.insert(Options, action_index)
    Options()
    
#load Options 
def Options():
    for child in body_win.winfo_children():
        child.destroy()
    create_options(body_win, w, h)
    Market_button.configure(bg = top_bar_color)
    Watchlist_button.configure(bg = top_bar_color)
    Options_Button.configure(bg = win_color)
    Correlations_Button.configure(bg = top_bar_color)

#load Correlations and add to LinkedList
def addCorrelations():
    global action_index
    action_index += 1
    track_action.insert(Correlations, action_index)
    Correlations()

#load Correlations
def Correlations():
    for child in body_win.winfo_children():
        child.destroy()
    create_correlations(body_win, w, h)
    Market_button.configure(bg = top_bar_color)
    Watchlist_button.configure(bg = top_bar_color)
    Options_Button.configure(bg = top_bar_color)
    Correlations_Button.configure(bg = win_color)
    
top_bar_color='grey18'
win_color='grey26'
buttonOn_color='grey30'

display = "Sign In / Sign Up"

#create window
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

Market_button = tk.Button(master = top_win, text = 'Market', font = "Calibri 20", command = addMarket)
Market_button.configure(background = top_bar_color, activebackground = buttonOn_color)

Watchlist_button = tk.Button(master = top_win, text = 'Watchlist', font = "Calibri 20", command = addWatchlist)
Watchlist_button.configure(background = top_bar_color, activebackground = buttonOn_color)

Options_Button = tk.Button(master = top_win, text = 'Options', font = "Calibri 20", command = addOptions)
Options_Button.configure(background = top_bar_color, activebackground = buttonOn_color)

Correlations_Button = tk.Button(master = top_win, text = 'Correlations', font = "Calibri 20", command = addCorrelations)
Correlations_Button.configure(background = top_bar_color, activebackground = buttonOn_color)

title_label.place(x = w*.08, y = h*.005)
search_button.place(x = w*.26, y = h*.014, width = w*.065, height = h*.03)
search_bar.place(x = w*.26 + w*.065 , y = h*.014, width = w*.46, height = h*.03)
profile_button.place(x = w*.78, y = h*.014, height = h*.03)

back_button.place(x = w*.008, y = h*.059, width = w*.016)
forward_button.place(x = w*.008 + w*.016 , y = h*.059, width = w*.016)
Market_button.place(x = w*.21, y = h*.059, width = w*.082, height = h*.058)
Watchlist_button.place(x = w*.42, y = h*.059, width = w*.082, height = h*.058)
Correlations_Button.place(x = w*.63, y = h*.059, width = w*.087, height = h*.058)
Options_Button.place(x = w*.84, y = h*.059, width = w*.082, height = h*.058)

#body
body_win = tk.Frame(master = window, width = w, height = h - h*.118)
body_win.pack_propagate(False)
body_win.configure(bg = win_color)
body_win.pack()

#display market in body on startup
addMarket()

window.mainloop()