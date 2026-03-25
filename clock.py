import datetime
import pytz

class DigitalClock:
    def __init__(self):
        self.timezones = {
            'UTC': pytz.utc,
            'America/New_York': pytz.timezone('America/New_York'),
            'Europe/London': pytz.timezone('Europe/London'),
            'Asia/Tokyo': pytz.timezone('Asia/Tokyo'),
            'Australia/Sydney': pytz.timezone('Australia/Sydney')
        }

    def get_time(self, timezone_name):
        if timezone_name in self.timezones:
            tz = self.timezones[timezone_name]
            return datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        else:
            raise ValueError('Timezone not recognized')

    def display_times(self):
        print('Current times in different time zones:')
        for timezone in self.timezones:
            print(f'{timezone}: {self.get_time(timezone)}')

if __name__ == '__main__':
    clock = DigitalClock()
    clock.display_times()