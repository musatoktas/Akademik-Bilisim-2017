class rehber:
    def __init__(self):
        self.kisiler = {}

    def ekle(self, kisi):
        self.kisiler[kisi.eposta] = kisi

    def epostaya_gore_ara(self, eposta):
        if eposta in self.kisiler.keys():
            return self.kisiler[eposta]
        return "bulunamadi"