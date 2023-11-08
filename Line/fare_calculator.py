import math
from datetime import datetime, timedelta

class Time:
    def __init__(self, timestamp):
        self.timestamp = datetime.strptime(timestamp, '%H:%M:%S.%f')

    @staticmethod
    def is_night_time(timestamp):
        night_start = timestamp.replace(hour=22, minute=0, second=0, microsecond=0)
        night_end = timestamp.replace(hour=5, minute=0, second=0, microsecond=0)
        return timestamp >= night_start or timestamp < night_end

class Record:
    def __init__(self, timestamp, distance):
        self.time = Time(timestamp)
        self.distance = distance

class FareCalculator:
    BASE_FARE = 410
    DISTANCE_RATE = 80
    DISTANCE_UNIT = 237
    SLOW_SPEED = 10
    SLOW_RATE = 80
    SLOW_UNIT = timedelta(minutes=1, seconds=30)
    NIGHT_MULTIPLIER = 1.25
    
    def __init__(self):
        self.total_distance = 0
        self.total_fare = self.BASE_FARE
        self.total_slow_time = timedelta()
    
    def calculate_fare(self, records):
        for i in range(1, len(records)):
            self._calculate_segment_fare(records[i-1], records[i])
        return self.total_fare
    
    def _calculate_segment_fare(self, prev_record, current_record):
        # Calculate distance fare
        distance = current_record.distance
        self.total_distance += distance
        if self.total_distance > 1052:
            extra_distance = self.total_distance - 1052
            units = math.ceil(extra_distance / self.DISTANCE_UNIT)
            self.total_fare += units * self.DISTANCE_RATE
        
        # Calculate slow speed fare
        time_diff = current_record.time.timestamp - prev_record.time.timestamp
        if time_diff.total_seconds() / 3600 * 1000 <= self.SLOW_SPEED:
            self.total_slow_time += time_diff
            while self.total_slow_time >= self.SLOW_UNIT:
                self.total_slow_time -= self.SLOW_UNIT
                self.total_fare += self.SLOW_RATE
        
        # Calculate night fare
        if Time.is_night_time(prev_record.time.timestamp):
            self.total_fare = int(self.total_fare * self.NIGHT_MULTIPLIER)

class Ride:
    def __init__(self, records):
        # records変数の各要素をスペースで分割してタイムスタンプと距離に分ける
        self.records = [Record(timestamp, float(distance)) for timestamp, distance in (record.split() for record in records)]
        self.fare_calculator = FareCalculator()
    
    def calculate_total_fare(self):
        return self.fare_calculator.calculate_fare(self.records)



import sys

# 入力行を読み込むための関数
def read_input():
    lines = []
    for line in sys.stdin:
        if line.strip():  # 空行でなければ追加
            lines.append(line.strip())
        else:  # 空行なら入力終了
            break
    return lines



records_input = read_input()

print(records_input)

ride = Ride(records_input)
total_fare = ride.calculate_total_fare()
print(total_fare)
