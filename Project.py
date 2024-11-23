import random
import os
class ceritaku:
    def __init__(self):
        Lauk = [ "Ayam bakar", "Rendang", "Dendeng Balado", "Ayam pop"]
        randomlauk = random.choice(Lauk)

        Rumahmakan= ["Payakumbah", "Pagi Sore"]
        randomRumahmakan = random.choice(Rumahmakan)

        Lauk2= ["Daun singkong", "Sambal merah","Sambal hijau"]
        randomlauk2 = random.choice(Lauk2)
        minuman =["Es Teh", "Jus jeruk", "air mineral"]
        randomminuman = random.choice(minuman)
        os.system("cls")
        print(f"Saya Makan nasi padang, piring dihidangangkan di atas meja dengan berbagai lauk,saya makan nasi padang dengan lauk {randomlauk} dan {randomlauk2} saya memesan miniuman {randomminuman} saya Makan nasi padang di {randomRumahmakan}")
def main():
    run = ceritaku()

if __name__ == "__main__":
    main()