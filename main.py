import tappedout
import sys
import pprint
import detect_shapes

image = "images/test.png"
url = sys.argv[1]

deck = tappedout.generateDeck(url)
status = detect_shapes.boardParser(image, deck)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(deck)
