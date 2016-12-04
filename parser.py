class BState:
    def __init__ (self, l, p, n):
        self.life = l
        self.poison = p
        self.names = n

def parse(input):
    print('Now parsing some shit')
    state = 0
    life_string = ""
    poison_string = ""
    cur_name = ""
    names = []
    for c in input:
        if state == 0 and c == '%':
            state = 1
        elif state == 1 and c != '%':
            life_string = life_string + c
        elif state == 1 and c == '%':
            state = 2
        elif state == 2 and c != '%':
            poison_string = poison_string + c
        elif state == 2 and c == '%':
            state = 3
        elif state == 3 and c != '&':
            cur_name = cur_name + c
        elif state == 3 and c == '&':
            state = 4
        elif state == 4:
            names.append((cur_name,int(c)))
            print(c)
            cur_name = ""
            state = 3
    return BState(int(life_string), int(poison_string), names)
"""bs = parse("%15%4%Swamp&1Swamp&0Swamp&1Doomed Necromancer&1")
print('The life is: ', bs.life)
print('The poison counters are: ', bs.poison)
for card,tapped in bs.names:
    if tapped:
        print(card, ' is tapped')
    if not tapped:
        print(card, ' is not tapped')"""
