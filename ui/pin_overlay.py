from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal

class PinOverlay(QWidget):
    unpin_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.pin_btn = QPushButton("📌")
        self.pin_btn.setCheckable(True)
        self.pin_btn.setChecked(True) # Always checked in overlay mode
        self.pin_btn.setFixedSize(25, 25)
        # Same style as TitleBar pin button
        self.pin_btn.setStyleSheet("""
            QPushButton { background: transparent; color: #888; border: none; border-radius: 3px; }
            QPushButton:checked { color: white; background-color: #28a745; }
            QPushButton:hover { color: white; background-color: #444; }
            QPushButton:checked:hover { background-color: #218838; }
        """)
        self.pin_btn.clicked.connect(self.on_click)
        self.layout.addWidget(self.pin_btn)
        
        self.setFixedSize(25, 25)

    def on_click(self):
        self.unpin_clicked.emit()
        self.close()
