class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.from_city == city or flight.to_city == city:
                result.append(flight)
        return result

    def search_from_city(self, from_city):
        result = []
        for flight in self.flights:
            if flight.from_city == from_city:
                result.append(flight)
        return result

    def search_between_cities(self, city1, city2):
        result = []
        for flight in self.flights:
            if (flight.from_city == city1 and flight.to_city == city2) or \
               (flight.from_city == city2 and flight.to_city == city1):
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight_table.add_flight(Flight(*data))

    while True:
        print("Options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            city = input("Enter city name: ")
            result = flight_table.search_by_city(city)
            for flight in result:
                print(f"Flight ID: {flight.flight_id}, From: {flight.from_city}, To: {flight.to_city}, Price: {flight.price}")
        elif choice == 2:
            from_city = input("Enter departure city name: ")
            result = flight_table.search_from_city(from_city)
            for flight in result:
                print(f"Flight ID: {flight.flight_id}, From: {flight.from_city}, To: {flight.to_city}, Price: {flight.price}")
        elif choice == 3:
            city1 = input("Enter first city name: ")
            city2 = input("Enter second city name: ")
            result = flight_table.search_between_cities(city1, city2)
            for flight in result:
                print(f"Flight ID: {flight.flight_id}, From: {flight.from_city}, To: {flight.to_city}, Price: {flight.price}")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()