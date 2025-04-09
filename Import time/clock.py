import time
from datetime import datetime

while True:
    current_time = datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute
    current_second = current_time.second
    print(f"It's {current_hour}:{current_minute}:{current_second} o'clock")

    time.sleep(3600 - current_time.minute * 60 - current_time.second)

