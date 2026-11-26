#Sözlük
#Sözlük oluşturma
#Sözlük yazdırma
#Sözlükteki verilere erişim
#Sözlükteki verileri düzenleme ve silme
#Sözlükte bir alan silme
#keys, value ve items metotları
#for dögüsü ile kullanımı

kisi = {"ad":"Efe", "soyad":"Altıntaş", "yas":20,"cinsiyet":"M", "Şehir":"İzmir","Hobiler" : ["Müzik","Spor","Kitaplar"]}

print(kisi["ad"]) #Sözlükteki verilere erişim
print(kisi["soyad"]) 
print(kisi["yas"])
print(kisi["cinsiyet"])

print(kisi)

kisi["ad"] = "Doruk" #Sözlükteki verileri düzenleme
print(kisi)

kisi.update({"ad":"Ahmet","yas":30}) #Aynı anda sözlükteki verileri düzenleme
print(kisi)

kisi["id"] = 101 #Sözlükte yeni bir alan ekleme
print(kisi)

del kisi["id"] #Sözlükte bir alan silme
print(kisi)

# DÖNGÜ
for baslik in kisi: #Sözlükteki alanları yazdırır
    print(baslik)
    
for a in kisi.keys(): #Sözlükteki alanları yazdırır
    print(a)


for b in kisi.values(): #Sözlükteki alanların değerlerini yazdırır
    print(b)

for deger in kisi: #Sözlükteki alanların değerlerini yazdırır
    print(kisi[deger]) 
# DÖNGÜ

print(kisi.keys()) #Sözlükteki alanları yazdırır
print(kisi.values()) #Sözlükteki alanların değerlerini yazdırır
print(kisi.items()) #Sözlükteki alanları ve değerlerini yazdırır

print(kisi["id"])   
print(kisi.get("id","Bulunamadı!..")) #Sözlükteki alanın değerini yazdırır. Eğer alan yoksa None döndürür.

