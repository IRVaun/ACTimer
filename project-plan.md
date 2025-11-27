Project Plan: Always-On-Top Timer App with 10-Minute Reminders (Custom UI Version)
1. Core Requirements
Start/Stop Timer: User can start the timer after a call and stop it anytime.
Soft Chime & Notification Every 10 Minutes: App plays a gentle sound and displays a notification every 10 minutes.
Reset While Running: User can reset the timer to zero, with the timer continuing afterward.
Pin ('Always on Top') & Transparency: App can be made always-on-top, with adjustable transparency for gaming or multitasking.
Custom, Frameless Window UI: The app uses a custom title bar integrated into a modern UI rather than the default OS window decorations.
2. Features Breakdown
Timer
Start, Stop, Reset controls as buttons in the main app window
Timer display (large, easy to read)
Notifications & Chime
Every 10 minutes: play a soft chime and display a system notification, even if app in background
Pin, Transparency, and Custom Window Controls
A ‘pin’ button in the app UI itself: toggles always-on-top behavior
‘Close’ and ‘minimize’ buttons integrated directly into the app’s own UI (not relying on OS title bar)
App window is frameless (removes standard Windows/Mac/Linux title bar)
Window can be dragged by clicking and dragging the app’s custom title area
Built-in transparency slider or toggle for quick adjustment
Polished Visual Design
Modern, uncluttered appearance, consistent color themes
Custom title bar styled to match the rest of the UI
Responsive/resizable window (as desired)
Visual feedback for pin/transparency status
3. UI Design Guidelines
No OS Title Bar: Use frameworks like PyQt to create a frameless window. Design a custom title bar as part of your app’s UI at the top, to contain minimize, close, and pin buttons, and allow window dragging.
Modern Look: Use flat or slightly rounded buttons, subtle shadows, and accent colors.
Simple, Intuitive: Prioritize easy accessibility of core functions; avoid over-complication.
Transparency Preview: When in transparent mode, timer display and controls should remain readable.
4. Technical Suggestions
Language & Framework: Python with PyQt5 or PyQt6 for strong custom window support.
System Notifications: Use cross-platform notification and audio libraries.
Custom Window Handling: Implement a QWidget as a title bar; handle mouse events for dragging and double-click for maximize/restore.
Settings/Preferences: Store user transparency, always-on-top, and other settings via simple file or appdata.
5. Development Steps
Setup Basic Frameless Window: Use PyQt's setWindowFlags(Qt.WindowType.FramelessWindowHint) for window with no OS title bar.
Design and Implement Custom Title Bar
Add custom minimize, close, and pin/always-on-top buttons in your UI.
Allow dragging the window by clicking the custom title area.
Build Main Timer UI
Timer logic and display.
Start/Stop/Reset buttons as part of app layout.
Add Notification & Chime Logic
Schedule chimes and notifications at 10-minute intervals.
Implement Pin & Transparency Features
Always-on-top toggle as a button on the custom title bar.
Adjustable transparency via slider or toggle.
Polish UI
Apply modern styling and transitions.
Ensure controls are visually integrated.
Testing
Test on Windows, macOS, and (optionally) Linux.
Verify window behavior, timer reliability, and notifications.
6. Reference UI Elements
Example: See modern timer apps with customized, borderless windows for inspiration.
Make sure window controls never rely on the OS title bar—everything accessible in your app’s look.