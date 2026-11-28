#listeler ile döngüleri
#range fonksiyonu ve for döngüsü
#iç içe for döngüleri
#break ve continue anahtarı
#while döngüsü

liste = [10,20,30,40,50,60]
isim = "Ahmet","Mehmet"
demet = (1,2,4,4,5,6)

#ÇIKTI
for sayi in liste:
    print(sayi)    
                     #Buradaki 3 döngüde'de liste ve demet elemanlarını yazdırırız.
for name in isim:
    print(name)

for rakam in demet:
    print(rakam)
#ÇIKTI


for a in range(0,10): #range fonksiyonu belirlenen aralıkta tekrar eder. İlk aralık dahildir son aralık dahil değildir!
    print(a)

for b in range(2,21,2): #İkiden başlayarak ikişer ikişer ilerler yirmide durur.
    print(b)


sonuc = 1
for c in range(10): #sadece tek bir sayı girildiğinde (0,10) olarak varsayılır.
    sonuc*=2
print(sonuc)  #0 dan başlayarak 9 kadar 10 kere 2 ile çarpılır ve sonuç toplanır cevap 2 üssü 10'dur


liste2 = ["a","b","c","d"]
liste3 = [1,2,3,4]


for harf in liste2:
    for tamsayi in liste3:
        print(harf,tamsayi)

#BREAK VE CONTİNUE

liste4 = [100,200,300,400,500,600,700,800]
for i in liste4:
    if i == 300:
        continue  #Burada eğer i 300 ise atlayarak devam et talimatı vermiş olduk

    if i ==700:
        break  #Burada ile eğer i 700 ise dur talimatı verdir.

    print(i)


liste5 = range(100)
for uc in liste5:   #Sayımın 3'e bölümünden kalan 0 değil ise devam et talimatı verdir. Bu sebep ile 3' bölünmeyenleri atlamış olduk.
    if uc %3 != 0: 
        continue

    if uc == 81: #81'e geldiğinde döngüden çık ve bitir.
     break

    print(uc)

#BREAK VE CONTİNUE


#While
x = 1
while x < 10:  #x değişkeni 10 sayısından küçük olduğu sürece +1 ekleyerek yazdır.
    print(x)
    x +=1  
print("x = ",x,", döngü bitti.")

y = 3
while x*y < 1000: #x ve y değişkeninin çarpımları 1000< olduğu sürece ikisinide 2 büyüterek döngüye devam et talimatı verdik.
    print(x,y)
    x+=2
    y+=2    

u = 1
while True:
   print(u)
   u+=1
   if u == 10000:  #10000 SINIRINA GELDİMİ DÖNGÜDEN ÇIK VE DURDUR.
       break

o = 1
while True:

    if o %2 == 0:  #o değişkeninin 2 ile bölümüden kalan 0 ise atla ve devam et ve yazdır ardında değişkene 1 ekle başa dön o değişkeni 1000 olduğunda dögüden çık
        o+=1
        continue
    print(o)

    o+=1
    if o == 1000:
        break
#While
