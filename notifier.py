import time
from plyer import notification
while(True):
  notification.notify(
    title="Drink Water!!",
    message="Water is important for your health",
    app_icon=None,
    timeout=10
    )
  time.sleep(30)