from fare_calculator import FareCalculator
from models import Record

def read_input():
   
    lines = []
    while True:
        try:
            line = input()
            if not line:
                break
            lines.append(line.strip())
        except EOFError:
            break
    return lines

def main():
    
    records_input = read_input()

    records = [Record(timestamp, float(distance)) for timestamp, distance in (record.split() for record in records_input)]
    fare_calculator = FareCalculator()
    total_fare = fare_calculator.calculate_fare(records)
    print("Total fare is: {}".format(total_fare))

if __name__ == '__main__':
    main()
