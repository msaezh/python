import binance

client = binance.Client(api_key="", api_secret="")
tickers = client.get_all_tickers()

# Bandas de  trabajo

lower_limit = # Escribir limite inferior
higher_limit = # Escribir limite superior

# Estado inicial (en este caso la primera acción será vender al valor higher_limit)

flag_compra = 0
flag_venta = 1

while True:
        
    tickers = client.get_all_tickers()
    valor_ETHUSDT = float(tickers[12]['price'])
        
    if (valor_ETHUSDT > higher_limit) & (flag_venta == 1):
        ETH_balance = float(client.get_asset_balance(asset='ETH').get('free'))
        ETH_balance_formateado = format(ETH_balance,'.4f')
        price_limit = str(higher_limit)
        client.order_limit_sell(
            symbol = 'ETHUSDT',
            quantity = ETH_balance_formateado,
            price = price_limit)
        print("OFERTA DE VENTA PUESTA EN MERCADO")
        flag_venta = 0
        flag_compra = 1
    elif (valor_ETHUSDT < lower_limit) & (flag_compra == 1):
        USDT_balance = float(client.get_asset_balance(asset='USDT').get('free'))
        USDT_buy = (1-(0.1/100))*USDT_balance
        valor_ETHUSDT = float(tickers[12]['price'])
        quantity = USDT_buy/valor_ETHUSDT
        quantity_formateada = format(quantity,'.4f')
        price_limit = str(lower_limit)
        client.order_limit_buy(
            symbol = 'ETHUSDT',
            quantity = quantity_formateada,
            price = lower_limit) 
        flag_compra = 0
        flag_venta = 1
    else:
        print("ESPERANDO AL MERCADO")
