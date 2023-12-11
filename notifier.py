from plyer import notification
import psutil
from time import sleep
import os
import json

# Checking for battery.
if psutil.sensors_battery() is None:
    print("Battery not detected!")
    exit()

# Checking if it is window or not.
if os.name != "nt":
    exit()

# Reading settings file
with open("./settings.json") as settings_file:
    settings = json.load(settings_file)

MAX_BATTERY_PERCENT = settings["MAX_BATTERY_PERCENT"]
MIN_BATTERY_PERCENT = settings["MIN_BATTERY_PERCENT"]
NOTIFICATION_TIMEOUT = settings["NOTIFICATION_TIMEOUT"]
BATTERRY_CHECK_INTERVAL = settings["BATTERRY_CHECK_INTERVAL"] #sec
NOTIFICATION = settings["NOTIFICATION"]


while (True):

    sleep(BATTERRY_CHECK_INTERVAL)
    
    if not NOTIFICATION:
        continue

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