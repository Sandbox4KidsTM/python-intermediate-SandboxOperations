# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:14:43 2018

@author: Mitch Labrenz
"""

import tkinter as tk
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.draw_content()
        
    def draw_content(self):
        self.button = tk.Button(self)
        self.button["text"] = "Say Hello"
        self.button["command"] = self.say_hi
        
        self.my_label = tk.Label(self)
        self.my_label["text"] = "Welcome to Sandbox Computers!"
        
        self.my_label.pack(side="top")        
        self.button.pack(side="top")

    def say_hi(self):
        print("Hello World!")
        
class TimerApp(tk.Frame):
    def __init__(self, master=None, seconds = 60):
        super().__init__(master)
        self._init_secs = seconds
        self._is_running = True
        self._seconds = seconds
        self._paused = False
        self.pack()
        self.draw_timer()
        
    def draw_timer(self):
        self._t = tk.StringVar()
        self._t.set(str(self._seconds))
        self.time_label = tk.Label(self)
        self.time_label["textvariable"] = self._t
        self.time_label.config(font=("Courier", 44))
        self.time_label.pack()
        
        self.pause_bttn = tk.Button(self)
        self.pause_bttn.config(width=25, background="green", activebackground="#00AA00")
        self.pause_bttn["text"] = "Pause Timer"
        self.pause_bttn["command"] = self.pause_timer
        self.pause_bttn.pack()
        
        self.reset_btn = tk.Button(self)
        self.reset_btn["text"] = "Reset Timer"
        self.reset_btn["command"] = self.reset_timer
        self.reset_btn.pack()
        
        self.run_timer()
    
    def run_timer(self):
        if self._seconds > 0:
            self._t.set(self._seconds)
            if not self._paused:
                self._seconds -= 1
            self.after(1000, self.run_timer)
        else:
            self._t.set("Timer Done!")
            self._is_running = False
            
    def pause_timer(self):
        self._paused = not self._paused
        
    def reset_timer(self):
        self._seconds = self._init_secs
        if not self._is_running:
            self.run_timer()
    
    
root = tk.Tk()
app = TimerApp(root)
app.mainloop()