import requests
import datetime
all_pairs = [
    # "EURUSD",
    # "GBPUSD", "AUDUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY",
    # "EURGBP", "EURAUD", "EURNZD", "EURCAD", "EURCHF", "EURJPY", "CHFJPY",
    # "GBPAUD", "GBPNZD", "GBPCAD", "GBPCHF", "GBPJPY", "CADCHF", "CADJPY",
    # "AUDNZD", "AUDCAD", "AUDCHF", "AUDJPY", "NZDCAD", "NZDCHF", "NZDJPY"
]
all_pair = [
    "EURUSD",
    "GBPUSD", "AUDUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY",
    "EURGBP", "EURAUD", "EURNZD", "EURCAD", "EURCHF", "EURJPY", "CHFJPY",
    "GBPAUD", "GBPNZD", "GBPCAD", "GBPCHF", "GBPJPY", "CADCHF", "CADJPY",
    "AUDNZD", "AUDCAD", "AUDCHF", "AUDJPY", "NZDCAD", "NZDCHF", "NZDJPY"
]
seasonality_data = {

}
today = datetime.date.today()


def get_seasonality_data(pair):

    pair_seasonality_data = {
        "01": {},
        "02": {},
        "03": {},
        "04": {},
        "05": {},
        "06": {},
        "07": {},
        "08": {},
        "09": {},
        "10": {},
        "11": {},
        "12": {},
    }

    r = requests.get(f'https://prash.site/d3d-market-scanner//historical/{pair}.json')
    data = r.json()

    for i in pair_seasonality_data.keys():
        change_total = 0
        for j in range(10):
            change = float(data[f"{i}/01/{today.year - 10 + j}"]["Change %"].replace("%", ""))
            change_total += change
        pair_seasonality_data[i]["10-years"] = round(change_total / 10, 2)

    for i in pair_seasonality_data.keys():
        change_total = 0
        changes_list = []
        for j in range(5):
            change = float(data[f"{i}/01/{today.year - 5 + j}"]["Change %"].replace("%", ""))
            changes_list.append(change)
            change_total += change
        pair_seasonality_data[i]["5-years"] = round(change_total / 5, 2)

    for j in pair_seasonality_data.keys():
        try:
            change = float(data[f"{j}/01/{today.year}"]["Change %"].replace("%", ""))
            pair_seasonality_data[j]["this-year"] = change
        except KeyError:
            pass

    return pair_seasonality_data


# for pair in all_pairs:
#     seasonality_data[pair] = get_seasonality_data(pair)
