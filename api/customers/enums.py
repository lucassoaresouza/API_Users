from enum import Enum


class Classifications(str, Enum):
    ESPECIAL = 'especial'
    NORMAL = 'normal'
    LABORIOUS = 'laborious'


class Genders(str, Enum):
    FEMALE = 'f'
    MALE = 'm'


class Regions(str, Enum):
    MIDDLE = 'centro'
    MIDWEST = 'centro-oeste'
    MIDEAST = 'centro-leste'
    MIDSOUTH = 'centro-sul'
    MIDNORTH = 'centro-norte'
    NORTH = 'norte'
    NORTHEAST = 'nordeste'
    EAST = 'leste'
    SOUTHEAST = 'sudeste'
    SOUTH = 'sul'
    SOUTHWEST = 'sudoeste'
    WEST = 'oeste'
    NORTHWEST = 'noroeste'


class Nationalities(str, Enum):
    BRAZILIAN = 'BR'
