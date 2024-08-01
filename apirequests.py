import requests, json
import alpaca_trade_api as tradeapi
api_key = 'PKN6CJ6XS53H57S96Y2G'
api_secret = 'yYvOH5bObLd2cv8C4Fke1rSVzE5iYAbsv6bOE0Sx'
# Replace with your Alpaca API key and secret
base_url='https://paper-api.alpaca.markets'
account_url='{}/v2/account'.format(base_url)
order_url='{}/v2/orders'.format(base_url)
header={'APCA-API-KEY-ID': api_key, 'APCA-API-SECRET-KEY': api_secret}
def getaccount():
    r=requests.get(account_url,headers=header)
    return json.loads(r.content)
def create_order(symbol,qty,side,type,time_in_force):
    data = {
        'symbol': symbol,
        'qty':qty,
        'side':side,
        'type':type,
        'time_in_force':time_in_force
    }
    r=requests.post(order_url,json=data,headers=header)
    return json.loads(r.content)

