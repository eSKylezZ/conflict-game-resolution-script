import tkinter as tk
from tkinter import messagebox, ttk
import winreg
import pystray
from PIL import Image, ImageDraw, ImageTk
import requests
from io import BytesIO
import subprocess
import webbrowser
import os

# Registry paths for each game, Each path will be checked to allow for compatiblity between 32bit and 64 bit OSs and differences between pre windows 8 and windows 10+
reg_paths = {
    "Conflict Desert Storm": [
        (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Classes\VirtualStore\MACHINE\SOFTWARE\Wow6432Node\Pivotal Games\Conflict Desert Storm\Device Settings"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Pivotal Games\Conflict Desert Storm\Device Settings")
    ],
    "Conflict Desert Storm 2": [
        (winreg.HKEY_CURRENT_USER, r"Software\Classes\VirtualStore\MACHINE\SOFTWARE\WOW6432Node\SCi Games\CDS II\Device Settings"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\SCi Games\CDS II\Device Settings")
    ],
    "Conflict Vietnam": [
        (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Classes\VirtualStore\MACHINE\SOFTWARE\WOW6432Node\SCi Games\Conflict Vietnam"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\SCi Games\Conflict Vietnam\Device Settings"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\SCi Games\Conflict Vietnam")
    ],
    "Conflict Global Storm": [
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Pivotal\Conflict Global\Device Settings"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Pivotal\Conflict Global\Device Settings")
    ]
}

# Define example resolutions for each game
example_resolutions = {
    "Conflict Desert Storm": {
        24: "1152x648",
        25: "1280x768",
        26: "1280x720",
        27: "1280x800",
        29: "1280x1024",
        30: "1360x768",
        31: "1360x1024",
        32: "1364x768",
        33: "1440x900",
        34: "1600x900",
        35: "1680x1050",
        36: "1776x1000",
        37: "1920x1080",
        16: "2560x1440",
        19: "3840x2160"
    },
    "Conflict Desert Storm 2": {
        34: "1152x648",
        37: "1280x720",
        40: "1280x768",
        43: "1280x800",
        46: "1280x960",
        52: "1360x768",
        55: "1360x1024",
        58: "1366x768",
        61: "1440x900",
        64: "1600x900",
        67: "1680x1050",
        70: "1776x1000",
        73: "1920x1080",
        66: "3840x2160"
    },
    "Conflict Vietnam": {
        34: "1152x648",
        37: "1280x720",
        40: "1280x768",
        43: "1280x800",
        46: "1280x960",
        52: "1360x768",
        55: "1360x1024",
        58: "1364x768",
        61: "1440x900",
        64: "1600x900",
        67: "1680x1050",
        70: "1776x1000",
        73: "1920x1080",
        66: "3840x2160"
    },
    "Conflict Global Storm": {
        34: "1152x648",
        37: "1280x720",
        40: "1280x768",
        43: "1280x800",
        46: "1280x960",
        52: "1360x768",
        55: "1360x1024",
        58: "1364x768",
        61: "1440x900",
        64: "1600x900",
        67: "1680x1050",
        70: "1776x1000",
        73: "1920x1080",
        66: "3840x2160"
    }
}

def get_reg_path(game):
    for root_key, reg_path in reg_paths[game]:
        try:
            winreg.OpenKey(root_key, reg_path, 0, winreg.KEY_READ)
            return root_key, reg_path
        except FileNotFoundError:
            continue
    raise FileNotFoundError(f"No valid registry path found for {game}")

def set_resolution(resolution_index, game):
    try:
        root_key, reg_path = get_reg_path(game)
        key = winreg.OpenKey(root_key, reg_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "ResolutionIndex", 0, winreg.REG_DWORD, resolution_index)
        winreg.CloseKey(key)
        messagebox.showinfo("Success", f"Resolution set to index {resolution_index} for {game}.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to set resolution for {game}: {e}")

def on_submit(game, entry):
    try:
        resolution_index = int(entry.get())
        print(f"Setting resolution index to: {resolution_index} for {game}")
        set_resolution(resolution_index, game)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

def show_overlay(resolution_index):
    def create_image():
        width = 64
        height = 64
        image = Image.new('RGB', (width, height), color1)
        dc = ImageDraw.Draw(image)
        dc.text((10, 10), f"Res: {resolution_index}", fill=color2)
        return image

    color1 = (0, 0, 0)
    color2 = (255, 255, 255)
    icon = pystray.Icon("Resolution Overlay", create_image(), "Resolution Overlay")
    icon.run()

def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.RequestException:
        return None

def open_url(url):
    webbrowser.open_new(url)

app = tk.Tk()
app.title("Set Resolution Index")
app.geometry("550x720")
app.resizable(False, False)  # Disable resizing

tab_control = ttk.Notebook(app)

games = ["Conflict Desert Storm", "Conflict Desert Storm 2", "Conflict Vietnam", "Conflict Global Storm"]
image_paths = [
    "images/CD-BoxArt.jpg",
    "images/CD2-BoxArt.jpg",
    "images/Vietnam-BoxArt.jpg",
    "images/Global-BoxArt.jpg"
]
urls = [
    ["https://github.com/eSKylezZ", "https://www.pcgamingwiki.com/wiki/Conflict:_Desert_Storm"],
    ["https://github.com/eSKylezZ", "https://www.pcgamingwiki.com/wiki/Conflict:_Desert_Storm_II"],
    ["https://github.com/eSKylezZ", "https://www.pcgamingwiki.com/wiki/Conflict:_Vietnam"],
    ["https://github.com/eSKylezZ", "https://www.pcgamingwiki.com/wiki/Conflict:_Global_Terror"]
]

# Create a new frame for the footer
footer_frame = tk.Frame(app, padx=20, pady=20)
footer_frame.grid(row=2, column=0, pady=10, sticky='ew')

# Create a new frame for the generic statement
statement_frame = tk.Frame(app, padx=20, pady=20)
statement_frame.grid(row=1, column=0, pady=10, sticky='ew')

# Add a paragraph to the new frame
statement_label = tk.Label(statement_frame, text="The Resolution Examples are examples and may vary based on your PC configuration, (Multi-Monitor, Aspect Ratio, etc...). This tool should help speed up the trial and error portion to find the correct number to set a higher resolution", wraplength=500, justify='center')
statement_label.grid(row=0, column=0, pady=10)

def update_footer(index):
    for widget in footer_frame.winfo_children():
        widget.destroy()
    
    footer_frame.columnconfigure(0, weight=1)
    footer_frame.columnconfigure(1, weight=1)
    footer_frame.columnconfigure(2, weight=1)
    
    # Script Created By
    script_label = tk.Label(footer_frame, text="Script Created By:", anchor='center', fg="orange", wraplength=250)
    script_label.grid(row=0, column=0, sticky='e', padx=1, pady=1)
    
    url1_label = tk.Label(footer_frame, text=urls[index][0], anchor='center', fg="blue", cursor="hand2", wraplength=350)
    url1_label.grid(row=0, column=1, pady=0, sticky='w')
    url1_label.bind("<Button-1>", lambda e, url=urls[index][0]: open_url(url))
    
    # PCGamingWiki Link
    pcgw_label = tk.Label(footer_frame, text="PCGamingWiki Link:", anchor='center', fg="orange", wraplength=250)
    pcgw_label.grid(row=1, column=0, sticky='e', padx=1, pady=1)
    
    url2_label = tk.Label(footer_frame, text=urls[index][1], anchor='center', fg="blue", cursor="hand2", wraplength=350)
    url2_label.grid(row=1, column=1, pady=0, sticky='w')
    url2_label.bind("<Button-1>", lambda e, url=urls[index][1]: open_url(url))

for i, game in enumerate(games):
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=game)
    
    # Column 1: Apply section
    frame_left = tk.Frame(tab, padx=20, pady=20)
    frame_left.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
    
    tk.Label(frame_left, text=f"Enter Resolution Index for {game}:", anchor='center').grid(row=0, column=0, pady=5)
    entry = tk.Entry(frame_left, justify='center')
    entry.grid(row=1, column=0, pady=2)
    
    tk.Button(frame_left, text="Apply", command=lambda g=game, e=entry: on_submit(g, e)).grid(row=2, column=0, pady=5)
    
    # Load and display the image from local path
    img_path = image_paths[i]
    if os.path.exists(img_path):
        img = Image.open(img_path)
        img = img.resize((200, 300), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
        img = ImageTk.PhotoImage(img)
        tk.Label(frame_left, image=img).grid(row=3, column=0, pady=5)
        frame_left.image = img  # Keep a reference to avoid garbage collection
    
    # Column 2: Examples
    frame_right = tk.Frame(tab, padx=20, pady=20)
    frame_right.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
    
    tk.Label(frame_right, text="Example Resolution Indexes:", anchor='center').grid(row=0, column=0, pady=5)
    for index, resolution in example_resolutions[game].items():
        tk.Label(frame_right, text=f"Index {index}: {resolution}", anchor='center').grid(row=index+1, column=0, pady=2)

tab_control.grid(row=0, column=0, sticky='nsew')

# Configure the grid to stretch the tabs
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Ensure the tabs fill the entire width
for i in range(len(games)):
    tab_control.tab(i, sticky='nsew')

# Update footer when tab changes
def on_tab_change(event):
    selected_tab = event.widget.index("current")
    update_footer(selected_tab)

tab_control.bind("<<NotebookTabChanged>>", on_tab_change)

# Initialize footer for the first tab
update_footer(0)

print("Starting Tkinter main loop")
app.mainloop()
print("Tkinter main loop ended")