import mambase
import utils

def try_all_german_date_formats(string):
    try:
        return utils.parse_and_format_date_german(string)
    except:
        return utils.parse_and_format_date_germanshort(string)

class TelekomCloud(mambase.RegexMetaDataCheck):
    __documentclass__ = "G - Rechnung"
    __tags__ = ["Telekom", "Hosting, E-Mail, Kommunikation"]
    __filter__ = lambda s, x: ("Telekom" in x and "TelekomCLOUD" in x)
    __meta__ = [
        {"metadata": "invoicer", "value": "Telekom Deutschland GmbH"},
        {
            "metadata": "invoicedate",
            "regex": "Rechnungsdatum:\\s+(.*)",
            "post": try_all_german_date_formats
        },
        {"metadata": "invoicenumber", "regex": "Rechnungsnummer:\\s+(.*)",},
        {"metadata": "amount", "regex": r"\d+,\d+$",},
    ]

class TelekomMobilfunk(mambase.RegexMetaDataCheck):
    __documentclass__ = ["G - Rechnung", "P - Rechnung"]
    __tags__ = ["Telekom", "Hosting, E-Mail, Kommunikation"]
    __filter__ = lambda s, x: ("Telekom" in x and "Mobilfunk" in x)
    __meta__ = [
        {"metadata": "invoicer", "value": "Telekom Deutschland GmbH"},
        {
            "metadata": "invoicedate",
            "regex": r"Datum\s+(\d{2}\.\d{2}\.\d{4})",
            "post": utils.parse_and_format_date_german,
        },
        {
            "metadata": "invoicedate",
            "regex": r"Datum\s+(\d{2}\.\d{2}\.\d{2})",
            "post": utils.parse_and_format_date_germanshort,
        },
        {"metadata": "invoicenumber", "regex": r"Rechnungsnummer\s+(.*)",},
        {"metadata": "amount", "regex": r"Rechnungsbetrag\s+(\d+,\d+)",},
    ]



__plugin__ = [TelekomCloud, TelekomMobilfunk]
