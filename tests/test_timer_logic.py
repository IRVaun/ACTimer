import unittest
import sys
from PyQt6.QtWidgets import QApplication
from core.timer_logic import TimerLogic

# Create QApplication instance for QTimer/Signals
app = QApplication(sys.argv)

class TestTimerLogic(unittest.TestCase):
    def setUp(self):
        self.logic = TimerLogic()

    def test_initial_state(self):
        self.assertEqual(self.logic.elapsed_seconds, 0)
        self.assertFalse(self.logic.is_running)

    def test_start_stop(self):
        self.logic.start()
        self.assertTrue(self.logic.is_running)
        self.logic.stop()
        self.assertFalse(self.logic.is_running)

    def test_reset(self):
        self.logic.elapsed_seconds = 10
        self.logic.reset()
        self.assertEqual(self.logic.elapsed_seconds, 0)

    def test_update_logic(self):
        # Manually trigger update to test logic without waiting for QTimer
        self.logic._update_time()
        self.assertEqual(self.logic.elapsed_seconds, 1)
        
        # Test 10 minute mark
        self.logic.elapsed_seconds = 599
        
        # We need to catch the signal
        self.signal_emitted = False
        def on_ten_min():
            self.signal_emitted = True
            
        self.logic.ten_minute_reached.connect(on_ten_min)
        self.logic._update_time()
        
        self.assertEqual(self.logic.elapsed_seconds, 600)
        self.assertTrue(self.signal_emitted)

if __name__ == '__main__':
    unittest.main()
