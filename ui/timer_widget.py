from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSlider
from PyQt6.QtCore import Qt, pyqtSignal
from core.timer_logic import TimerLogic

class TimerWidget(QWidget):
    transparency_changed = pyqtSignal(int) # 0-100

    def __init__(self, parent=None):
        super().__init__(parent)
        self.logic = TimerLogic()
        self.logic.time_updated.connect(self.update_time_display)
        self.logic.ten_minute_reached.connect(self.on_ten_minute_reached)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 5, 10, 10)
        self.layout.setSpacing(5)

        # Timer Display
        self.time_label = QLabel("00:00:00")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 32px; color: white; font-family: monospace;")
        self.layout.addWidget(self.time_label)

        # Controls
        self.controls_layout = QHBoxLayout()
        self.controls_layout.setSpacing(4)
        
        self.start_btn = QPushButton("Start")
        self.start_btn.clicked.connect(self.logic.start)
        self.controls_layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("Stop")
        self.stop_btn.clicked.connect(self.logic.stop)
        self.controls_layout.addWidget(self.stop_btn)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self.logic.reset)
        self.controls_layout.addWidget(self.reset_btn)

        self.layout.addLayout(self.controls_layout)

        # Transparency Slider
        self.slider_layout = QHBoxLayout()
        self.slider_layout.setSpacing(4)
        self.slider_label = QLabel("Opacity:")
        self.slider_label.setStyleSheet("color: #aaa; font-size: 10px;")
        self.slider_layout.addWidget(self.slider_label)

        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(40, 100) # Min 40% opacity
        self.opacity_slider.setValue(100)
        self.opacity_slider.setFixedHeight(16)
        self.opacity_slider.valueChanged.connect(self.transparency_changed.emit)
        self.slider_layout.addWidget(self.opacity_slider)

        self.layout.addLayout(self.slider_layout)

        # Styling
        self.setStyleSheet("""
            QPushButton {
                background-color: #444;
                color: white;
                border: none;
                padding: 4px 8px;
                border-radius: 3px;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QPushButton:pressed {
                background-color: #333;
            }
        """)

    def update_time_display(self, time_str):
        self.time_label.setText(time_str)

    def on_ten_minute_reached(self):
        from core.notifier import Notifier
        Notifier.notify_ten_minutes()
