import os

class Eczane:
    def __init__(self):
        self.ilaclar = {
            "Parasetamol": 20.0,
            "Ibuprofen": 25.0,
            "Antibiyotik": 50.0,
            "Vitamin C": 15.0,
            "Alerji İlacı": 30.0
        }
        self.sepet = {}

    def arka_plan_kirmizi(self):
        os.system('')  # Windows için gerekli
        print("\033[41m\033[30m", end="")  # Arka plan kırmızı, yazı siyah

    def ilaclari_goster(self):
        print("\nEczanemizde Bulunan İlaçlar:")
        for ilac, fiyat in self.ilaclar.items():
            print(f"{ilac} - {fiyat:.2f} TL")

    def ilac_ara(self, ilac_adi):
        if ilac_adi in self.ilaclar:
            print(f"{ilac_adi} mevcut, fiyatı: {self.ilaclar[ilac_adi]:.2f} TL")
        else:
            print(f"{ilac_adi} bulunamadı.")

    def sepete_ekle(self, ilac_adi, adet):
        if ilac_adi in self.ilaclar:
            if ilac_adi in self.sepet:
                self.sepet[ilac_adi] += adet
            else:
                self.sepet[ilac_adi] = adet
            print(f"{adet} adet {ilac_adi} sepete eklendi.")
        else:
            print(f"{ilac_adi} bulunamadı, sepete eklenemedi.")

    def sepeti_goster(self):
        if not self.sepet:
            print("\nSepetiniz boş.")
            return

        print("\nSepetinizdeki Ürünler:")
        toplam = 0
        for ilac, adet in self.sepet.items():
            fiyat = self.ilaclar[ilac] * adet
            toplam += fiyat
            print(f"{ilac} - {adet} adet - {fiyat:.2f} TL")
        print(f"Toplam Fiyat: {toplam:.2f} TL")

    def odeme_yap(self):
        if not self.sepet:
            print("Sepetiniz boş, ödeme yapılamaz.")
            return

        self.sepeti_goster()
        print("\nÖdeme alındı. Teşekkür ederiz!")
        self.sepet.clear()

# Programın Ana Akışı
eczane = Eczane()
eczane.arka_plan_kirmizi()

while True:
    print("\n--- Eczane Programı ---")
    print("1. İlaçları Göster")
    print("2. İlaç Ara")
    print("3. Sepete Ekle")
    print("4. Sepeti Göster")
    print("5. Ödeme Yap")
    print("6. Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        eczane.ilaclari_goster()
    elif secim == "2":
        ilac_adi = input("Aramak istediğiniz ilacın adını girin: ")
        eczane.ilac_ara(ilac_adi)
    elif secim == "3":
        ilac_adi = input("Sepete eklemek istediğiniz ilacın adını girin: ")
        adet = int(input("Adet girin: "))
        eczane.sepete_ekle(ilac_adi, adet)
    elif secim == "4":
        eczane.sepeti_goster()
    elif secim == "5":
        eczane.odeme_yap()
    elif secim == "6":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
