import sys
from modes import magazyn

filename = sys.argv[1]
items = sys.argv[2:]

magazyn(filename, *items)