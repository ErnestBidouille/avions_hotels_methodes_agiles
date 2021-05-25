import logging
from typing import Tuple, Union
from avions.Vol import Vol
from avions.Avion import Avion
from hotels.hotel import Hotel
from factory_check_and_book import FactoryCheckAndBook


class FacadeBookHoliday():
    @staticmethod
    def reserver_vacances(
            vol: Vol, hotel: Hotel,
            nb_personnes: int) -> Union[Tuple[Union[Avion, False]], int]:
        if vol._ville_arrivee != hotel.ville.nom:
            logging.info(
                'Reservation impossible, ce vol ne dessert pas la ville de l\'hotel donné'
            )
            return False, 0
        avion, prix = FactoryCheckAndBook.check_and_book(
            vol, hotel, nb_personnes)
        if avion:
            logging.info(
                f'Votre avion sera {avion} et vous paierez l\'hotel {prix}')
        else:
            logging.info(
                f'Il n\'y a pas de vol disponible malheureusement mais pour information l\'hotel coûte {prix}'
            )
        return avion, prix


