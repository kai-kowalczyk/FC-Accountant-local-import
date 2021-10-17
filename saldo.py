import sys
from classes import saldo

filename = sys.argv[1]
amount = sys.argv[2]
comment = sys.argv[3]

saldo(filename, amount, comment)


