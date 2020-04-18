import mambase
import utils

class PortoMetaData(mambase.RegexMetaDataCheck):
    __documentclass__ = "G - Rechnung"
    __tags__ = ["Porto", "Rechnung"]
    __filter__ = lambda s, x: ("Deutsche Post AG" in x)
    __meta__ = [
        {"metadata": "invoicer", "value": "Deutsche Post AG"},
        {
            "metadata": "invoicedate",
            "regex": "Belegdatum:\\s+(.*)",
            "post": utils.parse_and_format_date_german,
        },
        {"metadata": "invoicenumber", "regex": r"Belegnummer:\s+(\d*)",},
        {"metadata": "amount", "regex": r"Betrag\s+(\d+,\d+)",},
    ]

__plugin__ = [PortoMetaData]
