import sys
from modes import zakup

filename = sys.argv[1]
item_id = sys.argv[2]
price = sys.argv[3]
amount = sys.argv[4]

zakup(filename, item_id, price, amount)