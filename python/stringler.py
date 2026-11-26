mesaj = "Merhaba dünya"

mesaj = mesaj.upper() # upper değişkenin içindeki tüm striglerin büyük yazılmasını sağlar.
print(mesaj)

mesaj = mesaj.lower() # lower değişkenin içindeki tüm striglerin küçük yazılmasını sağlar.
print(mesaj)

mesaj = mesaj.capitalize() # capitalize yanlızca baş harfin büyük yazılmasını sağlar.
print(mesaj)

print(mesaj.startswith("Me")) # başlangıç ifadeyi kontrol eder.  (true/false)
print(mesaj.endswith("ya")) # sondaki ifadeyi kontrol eder.  (true/false)

print(len(mesaj)) # değişkenin içindeki string'in kaç ifadeden(tamsayı) oluştuğunu gösterir.

print("Efe" * 10) # yan yana olucak şekilde "Efe" ifadesini tekrarlar (10 Kere)

isim = "Efe"
yas = "20"

print("{} , {} yaşındadır.".format(isim,yas)) # format ifadesi ile print'in içine "isim" ve "yaş" değişkeninin içindeki verilerin ekrana yazılmasını sağlarız.
# Alternatif
print(f"{isim}, {yas} yaşındadır.")