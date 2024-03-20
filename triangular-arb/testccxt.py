import ccxt
import time

exchange = ccxt.kucoin({
    'enableRateLimit': True,
})
markets = exchange.load_markets()
symbols = exchange.symbols

print(exchange.fetch_tickers(['ALGO/USDT', 'ALGO/BTC'])['ALGO/BTC']['bid'])
orderbook = exchange.fetch_order_book ('ALGO/USDT')
# asks = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
# print(asks)

# symbols = ['ALGO/USDT', 'ALGO/BTC', 'ALGO/ETH', 'ETH/USDT', 'ETH/BTC', 'BTC/USDT']
# symbols = ['KCS/USDT', 'USDT/KCS']

# delay = 2 # seconds
# for symbols in exchange.markets:
#     print (exchange.fetch_order_book (symbols))
#     time.sleep (delay) # rate limit
# for symbol in symbols:
#     orderbook = exchange.fetch_order_book (symbol)
#     bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
#     ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
#     spread = (ask - bid) if (bid and ask) else None
#     print (exchange.id, 'market price', { 'bid': bid, 'ask': ask, 'spread': spread })

# delay = 2
# seconds = 120 
# start_time = time.time()

# while True:
#     current_time = time.time()
#     elapsed_time = current_time - start_time

#     symbols = ['ALGO/USDT', 'ALGO/ETH', 'ETH/USDT']
#     bids = []
#     asks = []
#     for symbol in symbols:
#         orderbook = exchange.fetch_order_book (symbols[0])
#         bids.append(orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None)
#         asks.append(orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None)
#         # bids[len(bids):] = [orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None]
#         # asks[len(asks):] = [orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None]
#     result = asks[0] * (1 / bids[1]) * (1/ bids[2])
#     opposite = asks[2] * asks[1] * (1 / bids[0])

#     print(result, opposite)

#     if elapsed_time > seconds:
#         break

#     time.sleep(delay)




# exchange.load_markets ()

# etheur1 = exchange.markets['ETH/EUR']      # get market structure by symbol
# etheur2 = exchange.market ('ETH/EUR')      # same result in a slightly different way
# print(etheur1)

# etheurId = exchange.market_id ('ETH/EUR')  # get market id by symbol
# print(etheurId)

# symbols = exchange.symbols                 # get a list of symbols
# symbols2 = list (exchange.markets.keys ()) # same as previous line

# print (exchange.id, symbols)               # print all symbols

# currencies = exchange.currencies           # a dictionary of currencies