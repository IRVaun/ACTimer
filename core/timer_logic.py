from PyQt6.QtCore import QTimer, QObject, pyqtSignal, QTime

class TimerLogic(QObject):
    time_updated = pyqtSignal(str)
    ten_minute_reached = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_time)
        self.elapsed_seconds = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.timer.start(1000)
            self.is_running = True

    def stop(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False

    def reset(self):
        self.elapsed_seconds = 0
        self._emit_time()
        # If running, it continues running from 0

    def _update_time(self):
        self.elapsed_seconds += 1
        self._emit_time()
        
        if self.elapsed_seconds > 0 and self.elapsed_seconds % 600 == 0:
            self.ten_minute_reached.emit()

    def _emit_time(self):
        # Format as HH:MM:SS
        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = self.elapsed_seconds % 60
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.time_updated.emit(time_str)
