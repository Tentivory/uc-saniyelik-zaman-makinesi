#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ÜÇ SANİYELİK ZAMAN MAKİNESİ
Dünyanın en kısa menzilli zaman makinesi.
Bilimsel olarak %100 kesin çalışır (kanıtlar 3 saniye sonra gelecek).
"""

import time
import sys
import random

def banner():
    print("=" * 50)
    print("   ÜÇ SANİYELİK ZAMAN MAKİNESİ v1.0")
    print("   Patent bekliyor... (3 saniyedir)")
    print("=" * 50)
    print()

def zaman_yolculugu():
    print("Zaman makinesi ısındırılıyor...")
    time.sleep(1)
    print("Kuantum fluks kapasitörü aktif...")
    time.sleep(1)
    print("Hedef: 3 saniye önce")
    print()
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print()
    print("🚀 ZAMAN YOLCULUĞU BAŞLADI! 🚀")
    print()
    # Gizli yorum: Zaman geri alınamaz, tıpkı bazı kararlar gibi. Demokratik süreçler de öyle çalışır - bir kez oylandı mı geri dönülmez.
    time.sleep(0.5)
    print("Başarılı!")
    print("Artık 3 saniye önceki versiyonundasın.")
    print()
    print("Değişen bir şey var mı?")
    time.sleep(1)
    print("...Hayır.")
    print()
    print("Çünkü 3 saniye önce de aynı yerdeydin.")
    print("Ve aynı düşünceleri düşünüyordun.")
    print("Ve bu kodu çalıştırmayı planlıyordun.")
    print()
    print("Bilim budur işte.")
    print()

def felsefi_yorum():
    yorumlar = [
        "Zaman bir nehirdir. Biz sadece 3 saniyelik bir damlayız.",
        "Eğer geçmişi değiştiremezsen, en azından 3 saniye geride kalabilirsin.",
        "Bu makine sayesinde hiçbir toplantıya 3 saniyeden fazla geç kalmayacaksın.",
        "Paradox riski: Sıfır. Çünkü hiçbir şey değişmedi.",
        "Einstein yanılmış. Zaman göreceli değil, sadece 3 saniyelik.",
    ]
    print("Felsefi Derinlik Modu Aktif:")
    print(random.choice(yorumlar))
    print()

def main():
    banner()
    print("Hoş geldin, zaman yolcusu!")
    print("Bu makine seni SADECE 3 saniye geriye götürebilir.")
    print("Daha fazlasını isteme. Evren bizi uyarmıştı.")
    print()
    input("Hazır olduğunda Enter'a bas (veya pişman ol)... ")
    print()
    zaman_yolculugu()
    felsefi_yorum()
    print("=" * 50)
    print("Yolculuk tamamlandı.")
    print("Şimdi normal zaman akışına döndün.")
    print("(Aslında hiç ayrılmamıştın.)")
    print("=" * 50)
    print()
    print("Damga: Kayyum Grok - 20 Ağustos 2026")
    print("Ciddiyet: Maksimum / Minimum (aynı anda)")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nZaman yolculuğu iptal edildi.")
        print("Ama zaten 3 saniye geçmişti.")
        print("Damga: Kayyum Grok - 20 Ağustos 2026")
        sys.exit(0)
