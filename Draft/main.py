import datetime
import time
import ntplib
import win32api

def main() -> None:
    conn = ntplib.NTPClient()
    timing = time.time()
    NTP_SERVER = "europe.pool.ntp.org"
    TIME_INTERVAL = 30
    response  = None

    while True:
        if time.time() - timing > TIME_INTERVAL:
            timing = time.time()
            
            try:
                response = conn.request (NTP_SERVER, version=3)
            except ntplib.NTPException:
                print (f"No response received from {NTP_SERVER}")

            if response:
                current_time = datetime.datetime.fromtimestamp(response.tx_time, datetime.timezone.utc)
                year = int (current_time.year)
                month = int (current_time.month)
                dayofweek = int (current_time.weekday())
                day = int (current_time.day)
                hour = int (current_time.hour)
                minute = int (current_time.minute)
                second = int (current_time.second)
                millisec = int (current_time.microsecond/1000)

                current_time = datetime.datetime.fromtimestamp(response.tx_time, datetime.timezone.utc)
                win32api.SetSystemTime(year, month, dayofweek, day, hour, minute, second, millisec)
                print (f"Sync at {current_time.time()}")
                response  = None

if __name__ == "__main__":
    main()
