import random, collections
def egit(metin):
kelimeler = metin.split()
model = collections.defaultdict(list)
for a, b in zip(kelimeler, kelimeler[1:]):
model[a].append(b) # a'dan sonra b geldi
return model
def uret(model, basla, n=8):
w, cikti = basla, [basla]
for _ in range(n):
w = random.choice(model[w]) # olasılıkla seç
cikti.append(w)
return " ".join(cikti)
>>> uret(egit(metin), "bir")
