from tradingview_ta import TA_Handler, Interval

technical_data = {}


def get_technical_data(pair):
    handler = TA_Handler(
        symbol=pair,
        exchange="FX_IDC",
        screener="forex",
        interval=Interval.INTERVAL_4_HOURS,
        timeout=None
    )
    technical_data[pair] = handler.get_analysis().summary


