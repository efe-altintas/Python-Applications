#if Operatörleri

#Eşittir "=="
#Eşit değildir "!="
#Büyüktür ">"
#Küçüktür "<"
#Büyük eşittir ">="
#Küçük eşittir "<="

#in not operatörleri
#and ve or bağlaç operatörleri
#is anahtarı(aynı nesneler olamalı)


if True:
     print("Koşul doğrudur.")

#Operator
a = 5
b = 7
if a < b:
    print("a b'den küçüktür.")

if a != b:
    print("a ile b eşit değildir.")
#Operator


#Operator
c = 10
d = 8
if c == d:
    print("c ile d eşittir.")
else :
    print("c ile d birbirine eşit değildir.")
#Operator


#Elif-Else
renk = "Turuncu"
if renk == "Turkuaz":
    print("Renk Turkuaz'dır.")

elif renk == "Mavi":
    print("Renk Mavi'dir.")

elif renk == "Lacivert":
    print("Renk Lacivert'dir.")
else:
    print("Hiçbiri")
#Elif-Else


#And-Or
e = 10
f = 5
g = 9

if e < g or g > f:   #Tek bir tanesinin doğru olması yeterdir. OR(veya)
    print("Koşul doğrudur.")
else:
    print("Koşul yanlıştır.")

if e > f and g == e and f < g: #Belirtilen tüm koşulların doğru olaması gerekir AND(ve)
    print("Koşul doğrudur.")
else:
    print("Koşul yanlıştır.")
#And-Or

#in
liste = [1,2,4,5,6,7]
h = 4
j = 9
if h in liste:
    print("Listede bulunuyor...")
else:
    print("Listede bulunmuyor!..")

if j in liste:
    print("Lisede bulunuyor...")
else:
    print("Listede bulunmuyor!..")


isim = "Efe"   #Harfler önemlidir küçük harf(e) ile büyük harf(E) farklı kabul edilir.
i = "E"
if i in isim:
    print("E bulunuyor...")
else:
    print("E bulunumadı!...")
#in

#NOT
if not i in isim:
    print("Listede vardır.") #Listede 'E' olmasına rağmen çıktıda yok görünür NOT kullanımı.
else:
    print("Listede yoktur.")


sayi1 = 10
sayi2 = 20              
if not sayi1 == sayi2:
    print("Koşul doğrudur.")
else:
    print("Koşul yanlıştır.")  #Çıktının koşul yanlıştır olması gerek fakat NOT kullandığımız için çıktı 'Koşul doğrudur.'
#NOT

#is
kelime1 = "python"
kelime2 = "java"

kelime2 += "n"
print(kelime1)
print(kelime2)

if kelime1 == kelime1:
    print("kelime1 = kelime2")
else:
    print("kelime1 != kelime2") 
    print(id(kelime1))
    print(id(kelime2))
#is