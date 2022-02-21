from decimal import Decimal


BR_BOUNDARIES = {
    "ESPECIAL": [
        {
            "minlon": Decimal("-2.196998"),
            "minlat": Decimal("-46.361899"),
            "maxlon": Decimal("-15.411580"),
            "maxlat": Decimal("-34.276938")
        },
        {
            "minlon": Decimal("-19.766959"),
            "minlat": Decimal("-52.997614"),
            "maxlon": Decimal("-23.966413"),
            "maxlat": Decimal("-44.428305")
        },
    ],
    "NORMAL": [
        {
            "minlon": Decimal("-26.155681"),
            "minlat": Decimal("-54.777426"),
            "maxlon": Decimal("-34.016466"),
            "maxlat": Decimal("-46.603598")
        }
    ]
}

BOUNDARIES_MAPPING = {
    'BR': BR_BOUNDARIES
}
