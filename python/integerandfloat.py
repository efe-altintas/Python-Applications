# İnteger tamsayı(16) gösteriminde float ise kesirli(11,5) sayıların gösteriminde kullanılır.

sayi1 = 5
sayi2 = 12.5
sayi3 = 22/7 
sayi4 = 6
sayi5 = 8
sayi6 = 100
sayi_6 = "100"
sayi7 = int(sayi_6)

print(sayi1)
print(sayi2)

print(type(sayi1)) # type ile değişkenin içindeki sayının türünü öğrenebiliriz
print(type(sayi2))

# Toplama "+"
# Çıkarma "-" 
# Çarpma "*"
# Bölme = "/"
# Tam Sayı Bölmesi = "//"
# Kuvvet Alma = "**"
# Mutlak Değer = "abs"

print (sayi1 + sayi2)
print (sayi1 - sayi2)
print (sayi1 * sayi2)
print (sayi1 / sayi2)
print (sayi1 // sayi2)

print(2**10)
print(16 / 5)
print(16 // 5)

print(abs(-2)) # abs hem float hem integer türünden girdi alabilir.
print(abs(-2.6))

print(round(sayi3))

print(3 * 5 + 10) # İşlem önceliği

# Eşittir "=="
# Eşit değildir "!="
# Küçüktür "<"
# Küçük eşit "<="
# Büyüktür ">"
# Büyük eşit ">="

print(sayi4 == sayi4) #True
print(sayi4 == sayi4) #True

print(sayi4 == sayi5) #False
print(sayi4 <= sayi5) #True
print(sayi4 >= sayi5) #False
print(sayi4 != sayi5) #True
# Farklı türlerdeki ifadelerde karşılaştırma yapılmaz.


#String ve Integer birbirine çevirme

print(type(sayi_6)) # str ifade
print(type(sayi6)) # int ifade
print(type(sayi7)) # sayi_6 ifadesinin integer türüne çevirilmiş halidir.

