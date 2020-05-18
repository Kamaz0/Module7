class AdressBook: 

    def __init__(self): 
        self.bizcards = []
    
    def add(self, biz_card):
        self.bizcards.append(biz_card)

    def show_all(self):
        for bizcard in self.bizcards:
            print(bizcard)

class BizCard: 
    
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
    
    def __str__(self):
        return f"<{self.name}, {self.surname}, {self.email}>"

    def __repr__(self):
        return str(self)

book = AdressBook()

viz_1 = BizCard("John", "Smith", "prezes@wuj.pl")
viz_2 = BizCard("Adam", "Ferency", "operator@kiepski.pl")
viz_3 = BizCard("Jan", "Kowalski", "profesjonalne_uslugi@buziaczek.pl")
viz_4 = BizCard("Lena", "Szalona", "jestem@szalona.pl")
viz_5 = BizCard("Apolonia", "Nowak", "egzotyczne@uslugi.pl")

book.add(viz_1)
book.add(viz_2)
book.add(viz_3)
book.add(viz_4)
book.add(viz_5)

all_wizytowki = (viz_1, viz_2, viz_3, viz_4, viz_5)

by_first_name = sorted(all_wizytowki, key=lambda biz_card: biz_card.name)
by_surname = sorted(all_wizytowki, key=lambda biz_card: biz_card.surname)
by_email = sorted(all_wizytowki, key=lambda biz_card: biz_card.email)

book.show_all()
print(by_first_name)
print(by_surname)
print(by_email)