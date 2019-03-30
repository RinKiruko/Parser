from DataUpdates.models import Cryptocurrency
from datetime import datetime as DateTime
from time import time
from collections import Counter


def get_profit(currency, buy_datetime, amount):           
    now = int(time.time())
    buy_timestamp = int(buy_datetime.timestamp())
    
    if buy_timestamp < currency.ListingDate.timestamp():
        return ValueError('Low time input')
    if buy_timestamp > now:
        return ValueError('Too high time input')

    deals = currency.Deals

    deals_iterator = iter(Deals.keys()))
    cur_timestamp = next(deals_iter)
    while cur_timestamp < buy_datetime:  
        cur_timestamp = next(deals_iter)    
    buy_timestamp = cur_timestamp

    buy_price = deals[buy_timestamp]
    prices = [deals[key] for key in deals_iterator]
    prices.append(buy_price)
    MaximumDealPrice = max(prices)
    MinimumDealPrice = min(prices)

    MaxPossibleProfit = (MaximumDealPrice - buy_price) * amount #Макс возможная прибыль
    MaxDrawdown = (buy_price - MinimumDealPrice) * amount #Макс просадка
    Profit = (deals.values()[-1] - buy_price) * amount #Прибыль
    return (Profit, MaxPossibleProfit, MaxDrawdown)


def get_count_trend_day(currency):
    trend_by_days = [day['Trend'] for day in Market.keys()]
    Distribution = Counter(trend_by_days)
    return Distribution


def get_currency_info(currency, date=None):
    try:
        for day in currency.Market.keys():
            volumes[day] = currency.Market[day]['Volume 24h']
        if date not None:            
            day_volume = volumes[date]
            return (currency.ListingDate, day_volume)
        return(volumes, currency.ListingDate)
    except KeyError:
        return ValueError('cant find that date or currency')
    return (currency.ListingDatem, volumes)


def compare_currency(first_currency, second_currency, buy_date):
    comparing_store = {}
    dispersion_1st_currency = disp(first_currency.Deals)
    dispersion_2nd_currency = disp(second_currency.Deals)
    
    if dispersion_1st_currency > dispersion_2nd_currency:
        comparing_store['Dispersion'] = {'win':second_currency, 'lose':first_currency}
    else:
        comparing_store['Dispersion'] = {'win':first_currency, 'lose':second_currency}
    
    max_possible_profit_1st, max_drawdown_1st = get_profit(first_currency, buy_date)
    max_possible_profit_2nd, max_drawdown_2nd = get_profit(second_currency, buy_date)
    if max_possible_profit_1st > max_possible_profit_2nd:
        comparing_store['MaxPossibleProfit'] ={'win': first_currency, 'lose':second_currency}
    else:
        comparing_store['MaxPossibleProfit'] ={'win': second_currency, 'lose':first_currency}    
    if max_drawdown_1st > max_drawdown_2nd:
        comparing_store['MaxPossibleProfit'] ={'win': second_currency, 'lose':first_currency}        
    else:
        comparing_store['MaxPossibleProfit'] ={'win': first_currency, 'lose':second_currency}
    
    volume_all_time_1st = sum(list(first_currency.Market[day]['Volume 24h'] for day in first_currency.Market.keys()))
    volume_all_time_2nd = sum(list(second_currency.Market[day]['Volume 24h'] for day in second_currency.Market.keys()))
    if volume_all_time_1st > volume_all_time_2nd:
        comparing_store['MaxVolume'] = {'win':first_currency, 'lose': second_currency}
    else:
        comparing_store['MaxVolume'] = {'win':second_currency, 'lose': first_currency}
    
    return comparing_store