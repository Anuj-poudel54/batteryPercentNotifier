from plyer import notification
import psutil
from time import sleep

MAX_BATTERY_PERCENT = 85
MIN_BATTERY_PERCENT = 45
NOTIFICATION_TIMEOUT = 15
BATTERRY_CHECK_INTERVAL = 120 #sec

while (True):
    battery_status = psutil.sensors_battery()
    if battery_status.power_plugged and battery_status.percent >= MAX_BATTERY_PERCENT:
        notification.notify(
        title = 'Disconnect the charger',
        message = f'Battery is {MAX_BATTERY_PERCENT}% full.',
        app_icon = None,
        timeout = NOTIFICATION_TIMEOUT,
    )
        
    elif not battery_status.power_plugged and battery_status.percent <= MIN_BATTERY_PERCENT:
        notification.notify(
        title = 'Connect the charger',
        message = f'Battery is less then {MIN_BATTERY_PERCENT}%.',
        app_icon = None,
        timeout = NOTIFICATION_TIMEOUT,
    )

    sleep(BATTERRY_CHECK_INTERVAL)

