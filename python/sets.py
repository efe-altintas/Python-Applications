#Küme nedir ve nasıl tanımlanır
#Kümeleri yazdırma
#Küme elemanları üstünde işlem yapma
#remove ve discard
#Kümelerde kesişim ve birleşim
#Kümelerde fark ve in anahtarı

kume = {"Sarı","Mavi","Kırmızı","Turuncu"}

print(type(kume))
print(len(kume))
print(kume)

kume.add("Turkuaz") #Turkazı kümeye ekler.
kume.remove("Sarı") #Sarıyı kümeden siler.
kume.discard("Gri") #Griyi kümeden siler. Eğer eleman yoksa hata vermez. Devamlılık sağlar.

#Kümeler sırasız veri yapılarıdır. Bu nedenle indeksleme ve dilimleme işlemleri yapılamaz.

for renk in kume:
    print(renk)

#Döngü her çalıştıpığında elemanların sırası değişebilir.

kume1 = {"1","22","12"}
kume2 = {"1","12","88"}

print(kume1.intersection(kume2)) #Kesişim kümesini verir.
print(kume1.union(kume2)) #Birleşim kümesini verir.
print(kume1.difference(kume2)) #Fark kümesini verir.

print("22" in kume1) #Küme içinde eleman var mı yok mu kontrol eder. True veya False döndürür.
print("22" in kume2) 

print("88" in kume1.union(kume2)) #İki kümenin birleşiminde elemanın var mı yok mu olduğunu kontrol eder.

boslist = [] #Boş bir liste oluşturur.
boslist2 = list() #Boş bir liste oluşturur.

bosdemet = () #Boş bir demet oluşturur.
bosdemet2 = tuple() #Boş bir demet oluşturur.

boskume = set() #Boş bir küme oluşturur.
boskume1 = {} #Bu bir sözlüktür. Boş bir küme oluşturmak için set() fonksiyonu kullanılmalıdır.

py = set("PYTHON")#Küme elemanları sırasızdır ve tekrarlayan elemanlar yoktur. Bu nedenle "P" harfi bir kez yazılır.
print(py) 