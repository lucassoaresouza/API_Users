from customers.enums import Regions


BR_REGIONS = {
    "acre": Regions.NORTH,
    "alagoas": Regions.NORTHEAST,
    "amapa": Regions.NORTH,
    "amazonas": Regions.NORTH,
    "bahia": Regions.NORTHEAST,
    "ceara": Regions.NORTHEAST,
    "distrito_federal": Regions.MIDWEST,
    "espirito_santo": Regions.SOUTHEAST,
    "goias": Regions.MIDWEST,
    "maranhao": Regions.NORTHEAST,
    "mato_grosso": Regions.MIDWEST,
    "mato_grosso_do_sul": Regions.MIDWEST,
    "minas_gerais": Regions.SOUTHEAST,
    "para": Regions.NORTH,
    "paraiba": Regions.NORTHEAST,
    "parana": Regions.SOUTH,
    "pernambuco": Regions.NORTHEAST,
    "piaui": Regions.NORTHEAST,
    "rio_de_janeiro": Regions.SOUTHEAST,
    "rio_grande_do_norte": Regions.NORTHEAST,
    "rio_grande_do_sul": Regions.SOUTH,
    "rondonia": Regions.NORTH,
    "roraima": Regions.NORTH,
    "santa_catarina": Regions.SOUTH,
    "são_paulo": Regions.SOUTHEAST,
    "sergipe": Regions.NORTHEAST,
    "tocantins": Regions.NORTH
}

COUNTRIES_REGIONS_MAPPING = {
    'BR': BR_REGIONS
}
