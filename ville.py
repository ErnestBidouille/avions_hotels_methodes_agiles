from typing import Iterable
from hotels.hotel import Hotel


class Ville:
    def __init__(self,
                 nom: str,
                 position_x: float,
                 position_y: float,
                 hotels: Iterable[Hotel] = None) -> None:
        self.nom = nom
        self.position_x = position_x
        self.position_y = position_y
        self.hotels = list()
        if hotels:
            self.add_hotels(hotels)

    def add_hotel(self, hotel: Hotel) -> None:
        self.hotels.append(hotel)
        hotel.ville = self

    def add_hotels(self, hotels: Iterable[Hotel]) -> None:
        for hotel in hotels:
            self.add_hotel(hotel)

