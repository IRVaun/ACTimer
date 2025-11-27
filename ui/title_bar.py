from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal

class TitleBar(QWidget):
    minimize_clicked = pyqtSignal()
    close_clicked = pyqtSignal()
    pin_toggled = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(24)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(4, 0, 4, 0)
        self.layout.setSpacing(3)

        # Title
        self.title_label = QLabel("ACTimer")
        self.title_label.setStyleSheet("color: white; font-weight: bold; font-size: 11px;")
        self.layout.addWidget(self.title_label)
        
        self.layout.addStretch()

        # Pin Button
        self.pin_btn = QPushButton("📌")
        self.pin_btn.setCheckable(True)
        self.pin_btn.setFixedSize(20, 20)
        self.pin_btn.setStyleSheet("""
            QPushButton { background: transparent; color: #888; border: none; border-radius: 3px; }
            QPushButton:checked { color: white; background-color: #28a745; }
            QPushButton:hover { color: white; background-color: #444; }
            QPushButton:checked:hover { background-color: #218838; }
        """)
        self.pin_btn.toggled.connect(self.pin_toggled.emit)
        self.layout.addWidget(self.pin_btn)

        # Minimize Button
        self.min_btn = QPushButton("—")
        self.min_btn.setFixedSize(20, 20)
        self.min_btn.setStyleSheet("""
            QPushButton { background: transparent; color: #888; border: none; font-size: 12px; }
            QPushButton:hover { color: white; background: #444; }
        """)
        self.min_btn.clicked.connect(self.minimize_clicked.emit)
        self.layout.addWidget(self.min_btn)

        # Close Button
        self.close_btn = QPushButton("✕")
        self.close_btn.setFixedSize(20, 20)
        self.close_btn.setStyleSheet("""
            QPushButton { background: transparent; color: #888; border: none; }
            QPushButton:hover { color: white; background: #cc0000; }
        """)
        self.close_btn.clicked.connect(self.close_clicked.emit)
        self.layout.addWidget(self.close_btn)

        # Window dragging
        self.start_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.start_pos:
            delta = event.globalPosition().toPoint() - self.start_pos
            self.window().move(self.window().pos() + delta)
            self.start_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.start_pos = None
