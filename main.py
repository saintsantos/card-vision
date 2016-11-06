import parse_html.tappedout as tappedout
import sys
import pprint
import shape_detection.detect_shapes as detect_shapes

image = "test.png"
url = sys.argv[1]

deck = tappedout.generateDeck(url)

status = detect_shapes.boardParser(image, deck)


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(deck)
