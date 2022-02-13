import tkinter as tk
from tkinter import ttk
import random
import threading
import playsound
from tkinter import *
from PIL import ImageTk,Image
from http.server import HTTPServer, BaseHTTPRequestHandler

# HTTP server
class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()

        data = {
            "username": username,
            "clicks": combined_clicks
        }

        json_data = json.dumps(data)

        payload = bytes(json_data,"utf-8")

        self.wfile.write(payload)

        return

    def log_message(self, format, *args):

        return

# Defaults username to guest
username = "guest"

# Starts playing music
#playsound.playsound('mixin.mp3', block=False)

# The amount added per click
clickrate = 1

# Combined clicks between all players
combined_clicks = 0

# Clicks for just our user
count = 0

# Whether we want music to be playing
stop_music = False

# List splash texts
splash_text = ["its just a number you know.", "SO MANY E'S!! ", "gosh golly thats a lot of eggs!", "more lines than Voxany!" , "tkinter!", "it all starts with 2!", "E", "my man got 65 blocks, now hes in prison"]

# def play_music(file_name):
#     global enable_music
#
#     playsound.playsound(file_name)
#
#     while not stop_music:
#         time.sleep(1) # Check for stopping music every second
#
#     else:
#         return

# Resets counter

# ------------ TITLE SCREEN ------------

def new_game():
    # STARTS GAME
    global username

    # Sets username
    username = enter_username.get()

    print(username)

    # Creates server object
    server = HTTPServer(('localhost',5554),Serv)
    server_thread = threading.Thread(target = server.serve_forever)
    server_thread.start()

def join_game():
    # JOIN EXISTING GAME
    global username

    # Sets username
    username = enter_username.get()

    # Creates server object and thread
    server = HTTPServer(('localhost',5554),Serv)
    server_thread = threading.Thread(target = server.serve_forever)
    server_thread.start()



title_screen = tk.Tk()
title_screen.title("E Clicker :)")


enter_username_label = tk.Label(title_screen, text="Enter Username:")
enter_username_label.grid(column=1, row=0)

enter_username = tk.Entry(title_screen)
enter_username.grid(column=1, row=1)


# Submit username
new_game_button = ttk.Button(title_screen, text="Start Game", command = new_game)
new_game_button.grid(column=1, row=2)

ip_enter_label = ttk.Label(title_screen, text = "Enter IP for existing game:")
ip_enter = ttk.Entry(title_screen)
ip_enter.grid(column = 1, row = 4)

join_game_button = ttk.Button(title_screen, text="Join Game", command = join_game)
join_game_button.grid(column = 1, row = 5)

print("got here!")

title_screen.mainloop()



# ------------ MAIN LAYOUT ------------

def reset():
    global count


    count = 0

    count_label.configure(text=f' {count} E s')
    playsound.playsound('hitHurt.wav', block=False)

# Click button
def clicked(): # without event because I use `command=` instead of `bind`
    global count

    # Adds to ONLY our personal clicks
    count += clickrate

    count_label.configure(text=f' {count} E s ')
    playsound.playsound('click.wav', block=False)

    if count >= 21:

        label= tk.Label(windows, text="Advancment: haha meme go brrrrrr (get to 21 E s")
        label.grid(column=0, row=2)

    if count >= 100:
        label= tk.Label(windows, text="Advancment: a master upon E s (get to 100 E s")
        label.grid(column=0, row=3)

    if count >= 1000:
        label= tk.Label(windows, text="Advancment: wow you actually made it this far? (get to 1000 E s")
        label.grid(column=0, row=4)

# Open shop menu
def shop():
    label= tk.Label(windows, text="Shop")
    label.grid(column=3, row=0)
    button= ttk.Button(windows, text="5 E s per click: Costs 20 E s", command=buy_upgrade)
    button.grid(column=3, row=1)

# Buy upgrade
def buy_upgrade():
    global count
    global clickrate

    if count >= 20:

        clickrate = 5
        count -=20
        count_label.configure(text=f'{count} E s')
        plusE.configure(text=f'Add {clickrate} E s')

    else:
        label= tk.Label(windows, text="You don't have enough E s!")
        label.grid(column=3, row=2)


# Creates main window
windows = tk.Tk()
windows.title("E Clicker :)")

# Title
label = tk.Label(windows, text="E Clicker: ")
label.grid(column=0, row=0)

# Shows count total
combined_count_label = tk.Label(windows, text = f'{count} E s')
combined_count_label.grid(column=0, row=1)



# Add E button
plusE = ttk.Button(windows, text=f"Add {clickrate} E", command=clicked)
plusE.grid(column=2, row=0)

# Reset counter
resetbutt = ttk.Button(windows, text="Reset Counter", command=reset)
resetbutt.grid(column=2, row=1)

# Splash text
notinthegithub = tk.Label(windows, text=random.choice(splash_text))
notinthegithub.grid(column=1, row=0)

# Open shop
shop = ttk.Button(windows, text="Shop", command=shop)
shop.grid(column=2, row=2)

# Makes a loop for the code to run :D
windows.mainloop()

