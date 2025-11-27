from plyer import notification
import winsound

class Notifier:
    @staticmethod
    def notify_ten_minutes():
        # Play a system sound
        # winsound.MessageBeep(winsound.MB_ICONASTERISK)
        # Or a specific frequency beep if preferred, but MessageBeep is standard "ding"
        try:
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        except Exception:
            pass # Fallback if sound fails

        # Show notification
        try:
            notification.notify(
                title='ACTimer',
                message='10 minutes have passed!',
                app_name='ACTimer',
                timeout=5
            )
        except Exception as e:
            print(f"Notification failed: {e}")
