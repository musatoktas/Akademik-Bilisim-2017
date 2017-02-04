class BankaHesabi:
    def __init__(self):
        self.bakiye = 0

    def para_cek(self, tutar):
        self.bakiye = self.bakiye - tutar
        return self.bakiye

    def para_yatir(self, tutar):
        self.bakiye = self.bakiye + tutar
        return self.bakiye

    def bakiye_yazdir(self, tutar):
        print(self.bakiye)