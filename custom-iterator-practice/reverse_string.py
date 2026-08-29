class ReverseString:
    def __init__(self, text):
        self.text = text
        self.baslangic = len(text)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.baslangic < 0:
            raise StopIteration
        karakter = self.text[self.baslangic]
        self.baslangic -= 1
        return karakter

for harf in ReverseString("kedi"):
    print(harf)
        
        