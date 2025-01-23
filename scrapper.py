import requests
from bs4 import BeautifulSoup

fundamental_urls = {
    "interest-rate": "https://tradingeconomics.com/country-list/interest-rate?continent=world",
    "gdp-growth-rate": "https://tradingeconomics.com/country-list/gdp-growth-rate?continent=world",
    "inflation-rate": "https://tradingeconomics.com/country-list/inflation-rate?continent=world",
    "unemployment-rate": "https://tradingeconomics.com/country-list/unemployment-rate?continent=world"
}

cot_currency_codes = {
    "EUR": "099741",
    "GBP": "096742",
    "AUD": "232741",
    "NZD": "112741",
    "USD": "098662",
    "CAD": "090741",
    "CHF": "092741",
    "JPY": "097741",
}

fundamental_data = {}
cot_data = {}
retail_data = {}


def get_fundamental_data(data_type):
    r = requests.get(fundamental_urls[data_type], headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")
    table = soup.find("table", {"class": "table table-hover table-heatmap"})
    rows = table.find_all("tr")
    for row in rows:
        data = row.get_text().strip().splitlines()
        try:
            country = data[0].lower().replace(" ", "-")
            items = {"last": data[2], "previous": data[3], "date": data[4], "unit": data[5]}
            if country not in fundamental_data:
                fundamental_data[country] = {}
                fundamental_data[country][data_type] = items
            else:
                fundamental_data[country][data_type] = items
        except IndexError:
            pass


def get_cot_data(currency):
    url = f"https://www.tradingster.com/cot/legacy-futures/{cot_currency_codes[currency]}"
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")
    rows = (soup.find("tbody")).findAll("tr")
    row = rows[1].get_text().strip().splitlines()
    l, s = float(row[0].replace(",", "")), float(row[1].replace(",", ""))
    long = round((l / (l + s)) * 100, 1)
    short = round((s / (l + s)) * 100, 1)
    cot_data[currency] = {}
    cot_data[currency]["long"] = long
    cot_data[currency]["short"] = short


def get_retail_data():
    url = "https://www.myfxbook.com/community/outlook"
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")
    tables = soup.find_all("table", {"class": "table table-bordered table-vertical-middle text-center margin-top-5"})
    for table in tables:
        rows = table.find_all("tbody")
        for row in rows:
            data = row.get_text().splitlines()
            retail_data[data[2]] = {}
            retail_data[data[2]]["long"] = int(data[10].replace("%", ""))
            retail_data[data[2]]["short"] = int(data[4].replace("%", ""))
