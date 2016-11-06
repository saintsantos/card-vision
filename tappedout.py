from bs4 import BeautifulSoup
import urllib.request

#http://tappedout.net/mtg-decks/count-von-count-counting-on-counters/

def generateDeck(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('a', class_="qty board")
    deck = {}
    for x in data:
        card = {}
        card_name = x["data-name"]
        set_name = x["data-orig"]
        final_card_name = card_name.replace(" ", "_")
        set_code = set_name[len(set_name) - 4:len(set_name) - 1]
        card["set name"] = set_code
        card["type"] = x["data-category"]
        num = x.get_text()
        card["number"] = num[0]
    #print("".join([set_code, "/", final_card_name, ".jpg"]))
        card["image_location"] = "".join([set_code, "/", final_card_name, ".full", ".jpg"])
        deck[final_card_name] = card
    return deck
