import csv


today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}

with open('stockprice.txt', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])