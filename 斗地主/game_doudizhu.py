import 斗地主.cards as cards
demo=cards.deck(True)
demo_cards=demo.cards

d=cards.deck(True)
d.shuffle()
cards=d.cards
# print(cards)

player1=cards[3:20]
player2=cards[20:37]
player3=cards[37:54]
extra=cards[:3]

def order(demo_cards,player):
    num=[]
    for item in player:
        index=demo_cards.index(item)
        num.append(index)
    # print(num)
    #将一个列表按照另一个列表排序
    player=[x for _, x in sorted(zip(num, player))]
    # print(player)
    return player

player1=order(demo_cards,player1)
player2=order(demo_cards,player2)
player3=order(demo_cards,player3)
extra=order(demo_cards,extra)

print(player1)
print(player2)
print(player3)
print(extra)