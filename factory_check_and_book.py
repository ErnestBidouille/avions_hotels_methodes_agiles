import logging
from typing import Tuple, Union
from avions.Vol import Vol
from avions.Avion import Avion
from hotels.hotel import Hotel


class FactoryCheckAndBook():
    @staticmethod
    def check_and_book(vol: Vol, hotel: Hotel,
                       nb_personnes: int) -> Tuple[Union[Avion, False], int]:
        if not vol._lst_avion:
            logging.info('Pas d\'avion disponible')
            avion = False
        elif vol.is_max_passenger():
            logging.info('Il n\'y a plus de places disponibles pour ce vol')
            avion = False
        else:
            avion = vol._lst_avion[0]
        return avion, hotel.prix_total(nb_personnes)

