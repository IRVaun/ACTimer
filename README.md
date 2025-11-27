# ACTimer - Overlay Timer Application

## Quick Start
Double-click `ACTimer.exe` to run the application.

## Features
- **Timer**: Count-up timer with Start, Stop, Reset controls
- **10-Minute Reminders**: Audio chime and notification every 10 minutes
- **Pin Mode**: Click the pin button (📌) to enable "Always on Top" + click-through mode
  - When pinned, you can click through the timer to interact with windows behind it
  - Only the pin button remains clickable to unpin
- **Transparency**: Adjust window opacity (40-100%) with the slider

## Controls
- **Start/Stop/Reset**: Control the timer
- **Pin Button (📌)**: Toggle always-on-top and click-through mode
- **Opacity Slider**: Adjust window transparency
- **Minimize (—)**: Minimize to taskbar
- **Close (✕)**: Exit application
- **Drag**: Click and hold the title bar to move the window

## Building from Source
If you want to rebuild the executable:
1. Install dependencies: `py -m pip install -r requirements.txt`
2. Run build script: `build.bat`
3. Executable will be in `dist\ACTimer.exe`
