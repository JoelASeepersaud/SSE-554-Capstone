import tkinter as tk
import ttkbootstrap as ttk

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
    text=tk.Label(master = parent, text='testing options')
    text.pack()

