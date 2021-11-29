import random

class deck():
    def __init__(self,hasjoker=False,num=1):
        number = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
        attrs = ['红桃', '方块', '梅花', '黑桃']
        self.cards=[]
        for n in range(int(num)):
            for num in number:
                for a in attrs:
                    self.cards.append(a+num)
            if hasjoker == True:
                self.cards.append('joker')
                self.cards.append('Joker')

    def shuffle(self):
        random.shuffle(self.cards)


# d=deck()
# print(d.cards)
# d.shuffle()
# print(d.cards)




# attrs = ['heart', 'spade', 'club', 'diamond']  # 桃，杏，梅，方
