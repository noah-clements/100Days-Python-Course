from datetime import datetime as dt

class FlightData:
    #This class is responsible for structuring the flight data.
    # assumes that origin city is known and unnecessary
    def __init__(self, to_city: str, to_city_code: str, to_airport: str, departure_time: dt, nights_in_dest: int, price: float, stop_overs=0, via_city="", link_to_flight='') -> None:
        self.origin_city = "Boston-Logan(BOS)"
        self.destination_city = to_city
        self.dest_city_IATA = to_city_code
        self.dest_airport = to_airport
        self.departure_time = departure_time
        self.nights_in_destination = nights_in_dest
        self.price = price
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.link = link_to_flight

    def __str__(self) -> str:
        layover = ""
        if self.stop_overs > 0:
            layover = f"Flight has {self.stop_overs} stopover via {self.via_city}. "
        return f"Flight from {self.origin_city} to {self.destination_city}-{self.dest_airport}, " \
                f"at {self.departure_time} with {self.nights_in_destination} nights " \
                f"in {self.destination_city}. {layover}Price: ${self.price}" \
                f"\n\n{self.link}"