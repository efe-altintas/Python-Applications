# Liste oluşturma

renkler = ["kırmızı", "mavi", "yeşil", "sarı"]

print(type(renkler)) # Değişkenin tipini(List) verir.

print(len(renkler)) # Listedeki eleman sayısını verir.

# print(renkler[0]) # Listedeki ilk elemanı verir. Indexler 0'dan başlar.

# print(renkler[2:]) # Listedeki 2. indexten itibaren tüm elemanları gösterir.

# print(renkler[0:3:2]) # 0'dan 3. indexe kadar olan elemanları 2'şer atlayarak gösterir.  

#append metodu
#insert metodu
#remove metodu
#extend metodu
#pop metodu
#reverse metodu
#sort ve sorted metodları

renkler.append("turuncu") # append ile listeye yeni eleman ekleriz.
print(renkler)

renkler.insert(0,"lacivert") # insert ile istediğimiz indexe yeni eleman ekleriz.
print(renkler)

renkler.remove("yeşil")# remove ile listeden istediğimiz elemanı silebiliriz.
print(renkler) 

renkler.extend(["beyaz","pembe"]) # extend ile listeye birden fazla eleman ekleyebiliriz.
print(renkler)

renkler.pop() # pop listedeki son elemanı siler.
print(renkler)

renkler.reverse() # reverse ile listedeki elemanların sırasını tersine çeviririz.
print(renkler)  

renkler.sort() # sort ile listedeki elemanları alfabetik olarak sıralarız.
print(renkler)

liste = sorted(renkler) # sorted ile listedeki elemanları sıralarız fakat listeyi değiştirmez.
print(liste)
print(renkler)

#min, max ve in metodu
#sum kullanımı
#for döngüsü ile liste elemanlarını yazdırma
#enumerate
#listeyi str çevirme
#str listeye çevirme

sayilar = [5, 10, 15, 20, 25]

print(min(sayilar)) # min ile listedeki en küçük elemanı buluruz.
print(max(sayilar)) # max ile listedeki en büyük elemanı buluruz.
print("Siyah" in renkler) # in ile listedeki elemanın var olup olmadığını kontrol ederiz.

print(sum(sayilar)) # sum ile listedeki elemanların toplamını buluruz.

for renk in renkler:
    print(renk) # for döngüsü ile listedeki elemanları tek tek yazdırırız.

for sayi in sayilar:
    print(sayi) # for döngüsü ile listedeki elemanları tek tek yazdırırız.

print(list(enumerate(renkler))) # enumerate ile listedeki elemanların indexlerini ve elemanlarını yazdırırız.

stringrenkler = "*".join(renkler) # join ile listedeki elemanları birleştirip stringe çeviririz.
print(stringrenkler)

