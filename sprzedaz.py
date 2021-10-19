import sys
from modes import sprzedaz

filename = sys.argv[1]
item_id = sys.argv[2]
price = sys.argv[3]
amount = sys.argv[4]

sprzedaz(filename, item_id, price, amount)