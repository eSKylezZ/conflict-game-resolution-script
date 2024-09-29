# Conflict Game Resolution Setter

This Python script allows you to set the screen resolution for various games in the "Conflict" series by modifying the Windows registry. The script uses the `tkinter` library for the GUI, `winreg` for registry operations.

## Features

- **Registry Path Management**: Handles different registry paths for compatibility between 32-bit and 64-bit operating systems.
- **Resolution Setting**: Allows setting screen resolutions for supported games.
- **GUI Integration**: Uses `tkinter` for a user-friendly interface.

## Supported Games

- Conflict Desert Storm
- Conflict Desert Storm 2
- Conflict Vietnam
- Conflict Global Storm

## Example Resolutions

Each game has predefined example resolutions that can be set using the script. Here are some examples:

- **Conflict Desert Storm**: 1920x1080, 2560x1440, 3840x2160
- **Conflict Desert Storm 2**: 1280x720, 1920x1080, 3840x2160
- **Conflict Vietnam**: 1280x720, 1920x1080, 3840x2160
- **Conflict Global Storm**: 1280x720, 1920x1080, 3840x2160

These example may vary per system, I have seen different values accepted for 3840x2160 when additional monitors are plugged in, this tool makes it quicker for the trial and error portion to find the correct value without needing to use regedit.

## How to Use

1. **Run the Script**: Execute the script using Python.
2. **Select Game**: Choose the game for which you want to set the resolution.
3. **Set Resolution**: Select the desired resolution from the dropdown menu.
4. **Apply**: Click the "Set Resolution" button to apply the changes.

## Code Overview

### Imported Libraries

```python
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
import sys
```

### Registry Key Paths
```
    Conflict: Desert Storm Registries
        (HKEY_CURRENT_USER\SOFTWARE\Classes\VirtualStore\MACHINE\SOFTWARE\Wow6432Node\Pivotal Games\Conflict Desert Storm\Device Settings),
        (HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Pivotal Games\Conflict Desert Storm\Device Settings)

    Conflict: Desert Storm 2 Registries
        (HKEY_CURRENT_USER\Software\Classes\VirtualStore\MACHINE\SOFTWARE\WOW6432Node\SCi Games\CDS II\Device Settings),
        (HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\SCi Games\CDS II\Device Settings)

    Conflict: Vietnam Registries
        (HKEY_CURRENT_USER\SOFTWARE\Classes\VirtualStore\MACHINE\SOFTWARE\WOW6432Node\SCi Games\Conflict Vietnam),
        (HKEY_LOCAL_MACHINE\SOFTWARE\SCi Games\Conflict Vietnam\Device Settings),
        (HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\SCi Games\Conflict Vietnam)

    Conflict: Global Storm Registries
        (HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Pivotal\Conflict Global\Device Settings),
        (HKEY_LOCAL_MACHINE\SOFTWARE\Pivotal\Conflict Global\Device Settings)
```

### Dependencies

- pystray
- requests
- PyInstaller (Only used for building the .EXEs)

## Running the script

### Manual Run / Install steps

1. Download & Install Python - https://www.python.org/downloads/
2. Run the following command in CMD or Powershell, you may need to run the CLI as admin as you are making changes to the windows registry
   - pip install requests pystray
3. Download the full repo or just the python script **resolution-script.py**
4. Within the same directory as the downloaded script run the following command
   - python ./resolution-script.py

### EXE Run

1. Download the correct build version for your operating system x64 for 64bit or x86 for 32bit
2. Run the exe, You may need to run as admin as you are making changes to the windows registry
   1. When running the EXE windows will warn its unsigned.


### Example of Script

![Example of script interface](/images/RI-Example.jpg "RI Example")
