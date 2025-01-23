from scrapper import *
from technical import *
from seasonality import *
from scoring import *

currency_map = {
    "EUR": "euro-area",
    "GBP": "united-kingdom",
    "AUD": "australia",
    "NZD": "new-zealand",
    "USD": "united-states",
    "CAD": "canada",
    "CHF": "switzerland",
    "JPY": "japan",
}


def summary_table(pair, label):
    base = pair[:3]
    quote = pair[3:]
    int_diff = float(fundamental_data[currency_map[base]]["interest-rate"]["last"]) - float(
        fundamental_data[currency_map[quote]]["interest-rate"]["last"])
    int_change_diff = (float(fundamental_data[currency_map[base]]["interest-rate"]["last"]) - float(
        fundamental_data[currency_map[base]]["interest-rate"]["previous"])) - (
                              float(fundamental_data[currency_map[quote]]["interest-rate"]["last"]) - float(
                          fundamental_data[currency_map[quote]]["interest-rate"]["previous"]))

    gdp_diff = float(fundamental_data[currency_map[base]]["gdp-growth-rate"]["last"]) - float(
        fundamental_data[currency_map[quote]]["gdp-growth-rate"]["last"])
    gdp_change_diff = (float(fundamental_data[currency_map[base]]["gdp-growth-rate"]["last"]) - float(
        fundamental_data[currency_map[base]]["gdp-growth-rate"]["previous"])) - (
                              float(fundamental_data[currency_map[quote]]["gdp-growth-rate"]["last"]) - float(
                          fundamental_data[currency_map[quote]]["gdp-growth-rate"]["previous"]))

    inf_diff = float(fundamental_data[currency_map[quote]]["inflation-rate"]["last"]) - float(
        fundamental_data[currency_map[base]]["inflation-rate"]["last"])
    inf_change_diff = (float(fundamental_data[currency_map[quote]]["inflation-rate"]["last"]) - float(
        fundamental_data[currency_map[quote]]["inflation-rate"]["previous"])) - (
                              float(fundamental_data[currency_map[base]]["inflation-rate"]["last"]) - float(
                          fundamental_data[currency_map[base]]["inflation-rate"]["previous"]))

    une_diff = float(fundamental_data[currency_map[quote]]["unemployment-rate"]["last"]) - float(
        fundamental_data[currency_map[base]]["unemployment-rate"]["last"])
    une_change_diff = (float(fundamental_data[currency_map[quote]]["unemployment-rate"]["last"]) - float(
        fundamental_data[currency_map[quote]]["unemployment-rate"]["previous"])) - (
                              float(fundamental_data[currency_map[base]]["unemployment-rate"]["last"]) - float(
                          fundamental_data[currency_map[base]]["unemployment-rate"]["previous"]))

    int_score = score_fundamental(int_diff, int_change_diff)
    gdp_score = score_fundamental(gdp_diff, gdp_change_diff)
    inf_score = score_fundamental(inf_diff, inf_change_diff)
    une_score = score_fundamental(une_diff, une_change_diff)
    cot_score = score_cot(cot_data[base], cot_data[quote])
    ret_score = score_retail(float(retail_data[pair]["long"]), float(retail_data[pair]["short"]))
    tec_score = score_technical(technical_data[pair])
    sea_score = score_seasonality(seasonality_data[pair][str(today.month).zfill(2)])
    total = round(int_score + gdp_score + inf_score + une_score + cot_score + ret_score + tec_score + sea_score, 0)
    if label:
        return pair, int_score, gdp_score, inf_score, une_score, cot_score, ret_score, tec_score, sea_score, total
    else:
        return int_score, gdp_score, inf_score, une_score, cot_score, ret_score, tec_score, sea_score, total


def fundamental_table(currency):
    locator = fundamental_data[currency_map[currency]]
    int = locator["interest-rate"]["last"]
    gdp = locator["gdp-growth-rate"]["last"]
    inf = locator["inflation-rate"]["last"]
    une = locator["unemployment-rate"]["last"]
    int_cng = round(float(locator["interest-rate"]["last"]) - float(locator["interest-rate"]["previous"]), 2)
    gdp_cng = round(float(locator["gdp-growth-rate"]["last"]) - float(locator["gdp-growth-rate"]["previous"]), 2)
    inf_cng = round(float(locator["inflation-rate"]["last"]) - float(locator["inflation-rate"]["previous"]), 2)
    une_cng = round(float(locator["unemployment-rate"]["last"]) - float(locator["unemployment-rate"]["previous"]), 2)
    return currency, f"{int}%", f"{int_cng}%", f"{gdp}%", f"{gdp_cng}%", f"{inf}%", f"{inf_cng}%", f"{une}%", f"{une_cng}%"


def cot_table(currency):
    return currency, f"{cot_data[currency]['long']}%", f"{cot_data[currency]['short']}%"


def retail_table(pair):
    return f"{retail_data[pair]['long']}%", f"{retail_data[pair]['short']}%"


def technical_table(pair):
    return technical_data[pair]["RECOMMENDATION"].replace("_", " "), technical_data[pair]["BUY"], technical_data[pair][
        "NEUTRAL"], technical_data[pair]["SELL"]
