import asyncio
import logging
import websockets
import names
from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK
import requests
from datetime import timedelta, date
from copy import deepcopy

logging.basicConfig(level=logging.INFO)


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects')

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distrubute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            if message == 'exchange':
                message = self.ex_rate_day ()
            if message == 'exchange 2':
                message = self.ex_rate_days ()
            await self.send_to_clients(f"{ws.name}: {message}")

    def ex_rate_day (self):
        response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
        exchange_rate = response.json()
        ex_str = ''
        for element in exchange_rate:
            ex_str += f"{element['ccy']}: Buy:{element['buy']} Sell:{element['sale']}; "
        return ex_str
    
    def ex_rate_days (self):
        results = []
        inpt_date = self.input_dates()
        for i in range(len(inpt_date)):
            response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={inpt_date[i]}')
            exchange_rate = response.json()
            date_result = self.parce (exchange_rate, inpt_date[i])
            results.append(date_result)
        return results

    def input_dates(self):
        scope = []
        inpt_depth = 5
        date_date = date.today()
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
    
    def parce (self, result, inpt_date):
        euro = {}
        doll = {}
        date_rates = {}
        date_result = {}

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
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 8080):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())