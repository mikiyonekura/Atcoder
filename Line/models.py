from datetime import datetime

class Time:
    def __init__(self, timestamp):
        self.timestamp = datetime.strptime(timestamp, '%H:%M:%S.%f')

class Record:
    def __init__(self, timestamp, distance):
        self.time = Time(timestamp)
        self.distance = distance
