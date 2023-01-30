import time
from plyer import notification

notification_title = 'Take a break!!!'
notification_message = '30 minutes passed ..please take take a break . Dont strain too much!!!!'

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False,
)
time.sleep(30)