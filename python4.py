
#Indexleme ve Dilimleme

kelime="Mutluluk"
print(kelime[0])    #ciktisi: M
#****************Indexler 0 dan baslar.******************
#Mutluluk 8 harflidir 8 eleman vardir.Son index 7 olur.
print(kelime[1])    #ciktisi: u
print(kelime[5])    #ciktisi: l
print(kelime[7])    #ciktisi: k
#print(kelime[8])   #ciktisi: index yok

kelime2=" Mutluluk" #basta bosluk oldugunu goruyoruz.
print(kelime2[0])   #ciktisi:' ' bosluktur.
print(kelime2[7])   #ciktisi: u
print(kelime2[8])   #ciktisi: k

#***************Indexler sondan -1 den baslar.*************

meslek="Muhendis"
print(meslek[-1])   #ciktisi: s 
print(meslek[-6])   #ciktisi: h

#Dilimleme(slicing)

#[baslangic:bitis:adim] 
#adim yazilmaz ise 1 dir.

print(meslek[0:3:2]) #ciktisi: Mh olur.Cunku baslangictan baslar 2 ser 2 ser ilerler ve bitis indexi dahil degildir.
print(meslek[1:3:2]) #ciktisi: u
#baslangic index degeri bitis index degerinden kucuk olmalidir cunku geri geri gidilmez.
#indexleme de 8 elemanli bir liste dusunelim son index 7 olacaktir ve biz 8. indexi istedigimiz zaman hata aliriz.
#Fakat slicing de boyle bir durum yoktur.Alacagi kadar eleman alir ve sonuna geldikten sonra bos donderir,hata vermez.
print(meslek[7:2:])   #bosluk donderir.
print(meslek[7:2:-1]) #sidne ciktisini dondurur.-1 sondan basla demektir.
print(meslek[::1])    #burada baslangıc da bitis de verilmemis.Bu bastan basla sona kadar devam et demektir.
