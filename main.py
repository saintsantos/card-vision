import parse_html.tappedout as tappedout
import sys
import pprint

url = sys.argv[1]

deck = tappedout.generateDeck(url)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(deck)
