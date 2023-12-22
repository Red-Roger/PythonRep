import platform

import aiohttp
import asyncio
from datetime import date, datetime, timedelta
from copy import deepcopy

date_result = {} 

def inpt():

    inpt_date = input ("Input date: (dd.mm.yyyy)")
    try:
        datetime.strptime(inpt_date, '%d.%m.%YYYY').date()
    except ValueError:
        inpt_date = input ("Date is not correct\nInput date: (dd.mm.yyyy)")
    inpt_depth = int (input ("Input depth: "))
    while ( inpt_depth > 10 or inpt_depth < 1 ):
        inpt_depth = int (input ("Input depth should be from -1 to 10\nInput depth: "))
    scope = input_dates(inpt_date, inpt_depth)

    return scope

def input_dates(inpt_date, inpt_depth):
    scope = []
    date_date = datetime.strptime(inpt_date, '%d.%m.%Y').date()
    for i in range(inpt_depth):
        str_day = str (date_date.day)
        str_month = str (date_date.month)
        if date_date.day < 10:
            str_day = f"0{date_date.day}"
        if date_date.month < 10:
            str_month = f"0{date_date.month}"
        str_date = f"{str_day}.{str_month}.{date_date.year}"
        scope.append(str_date)
        date_date = date_date - timedelta (days = 1)
    
    return scope

def parce (result, inpt_date):
    euro = {}
    doll = {}
    date_rates = {}

    rates = result['exchangeRate']
    for j in rates:
        if j['currency'] == "EUR":
            euro['sale'] = j['saleRate']
            euro['purchase'] = j['purchaseRate']
        if j['currency'] == "USD":
            doll['sale'] = j['saleRate']
            doll['purchase'] = j['purchaseRate']
    date_rates['EUR'] = euro
    date_rates['USD'] = doll
    date_result[inpt_date] = deepcopy(date_rates)
    return date_result


async def main():

    async with aiohttp.ClientSession() as session:
        results = []
        date_result = {}
        inpt_date = inpt()

        for i in range(len(inpt_date)):
            async with session.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={inpt_date[i]}') as response:
                result = await response.json()
            date_result = parce(result, inpt_date[i])
        results.append(date_result)
        return results


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)