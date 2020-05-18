class AdressBook: 

    def __init__(self): 
        self.bizcards = []
    
    def add(self, biz_card):
        self.bizcards.append(biz_card)

    def show_all(self):
        for bizcard in self.bizcards:
            print(bizcard)


class BaseContact: 
    
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"<{self.name}, {self.surname},{self.phone}, {self.email}>"

    def __repr__(self):
        return str(self)

    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}"

    @property
    def full_name(self):
        return f"{self.name}{self.surname}"

    @property
    def label_length(self):
        return len(self.full_name)


class BusinessContact(BaseContact):
    def __init__(self, position, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone

    def contact(self):
        return f"Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}"

    @property
    def full_name(self):
        return f"{self.name}{self.surname}"

    @property
    def label_length(self):
        return len(self.full_name)


book = AdressBook()

viz_1 = BaseContact("John", "Smith", "+48 123456789","prezes@wuj.pl")
biz_viz_1 = BusinessContact(name="Izajasz", surname="Goldbaum", phone="+48 234234234", email="tata@majaja.iz", position="Lecturer", company="University of Jerusalem", work_phone="+34 234234234")

print(viz_1.contact())
print(biz_viz_1.contact())
print(f"Długość liter pana powyżej: {biz_viz_1.label_length}")