from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from ui.title_bar import TitleBar
from ui.timer_widget import TimerWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(300, 250)

        # Central Widget
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("""
            QWidget#CentralWidget {
                background-color: #222;
                border: 1px solid #444;
                border-radius: 10px;
            }
        """)
        self.central_widget.setObjectName("CentralWidget")
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Title Bar
        self.title_bar = TitleBar(self)
        self.title_bar.minimize_clicked.connect(self.showMinimized)
        self.title_bar.close_clicked.connect(self.close)
        self.title_bar.pin_toggled.connect(self.toggle_always_on_top)
        self.layout.addWidget(self.title_bar)

        # Timer Widget
        self.timer_widget = TimerWidget(self)
        self.timer_widget.transparency_changed.connect(self.set_opacity)
        self.layout.addWidget(self.timer_widget)

    def toggle_always_on_top(self, checked):
        flags = self.windowFlags()
        
        if checked:
            # Enable Always on Top
            flags |= Qt.WindowType.WindowStaysOnTopHint
            # Enable Click-Through
            flags |= Qt.WindowType.WindowTransparentForInput
            
            # Show Overlay
            self.show_pin_overlay()
        else:
            # Disable Always on Top
            flags &= ~Qt.WindowType.WindowStaysOnTopHint
            # Disable Click-Through
            flags &= ~Qt.WindowType.WindowTransparentForInput
            
            # Hide Overlay (if it exists)
            if hasattr(self, 'pin_overlay') and self.pin_overlay:
                self.pin_overlay.close()
        
        self.setWindowFlags(flags)
        self.show()

    def show_pin_overlay(self):
        from ui.pin_overlay import PinOverlay
        
        # Get global position of the real pin button
        pin_btn = self.title_bar.pin_btn
        global_pos = pin_btn.mapToGlobal(pin_btn.rect().topLeft())
        
        self.pin_overlay = PinOverlay()
        self.pin_overlay.move(global_pos)
        self.pin_overlay.unpin_clicked.connect(self.on_overlay_unpin)
        self.pin_overlay.show()

    def on_overlay_unpin(self):
        # Sync state back to main window
        self.title_bar.pin_btn.setChecked(False)
        # toggle_always_on_top will be called by the signal from title_bar.pin_btn

    def set_opacity(self, value):
        self.setWindowOpacity(value / 100.0)
