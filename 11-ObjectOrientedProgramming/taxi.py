from typing import Self


class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    def print_recepit(self):
        print(f"The rate is {self.rate_per_km}")
        print(f"The distance is {self.distance}")
        print(f"The flare is {self.fare}")


def main():
    TaxiRide1 = TaxiRide(rate_per_km=2)
    TaxiRide1.calculate_fare(distance=10)
    TaxiRide1.print_recepit()
    print()
    TaxiRide2 = TaxiRide(rate_per_km=3)
    TaxiRide2.calculate_fare(distance=11)
    TaxiRide2.print_recepit()


    

if __name__ == "__main__":
    main()
