from enum import Enum


class Types(str, Enum):
    ESPECIAL = 'especial'
    NORMAL = 'normal'
    LABORIOUS = 'laborious'


class Genders(str, Enum):
    FEMALE = 'F'
    MALE = 'M'


class Regions(str, Enum):
    CENTER = 'centro'
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
