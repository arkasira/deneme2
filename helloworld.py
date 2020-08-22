# mesela liste olarak tanimlanan birsey 'obje' olarak isimlendirilir. Bunun icin yapabilecegin bir islem ise 
#metod olarak adlandirilir.

a=[1,2,3,4,5]
print(type(a))
a.insert(1,'Murat')
print(a)
a.append('Python')
print(a)
a.pop()
print(a)
#print bir fonksiyondur. ama bir method degildir. olusturulan liste bir objedir.
#foksiyon tanimlama

#def Fonksiyon_Adi(Parametre1,Parametre2):
    #Fonksiyon Blogu
    #Yapilacak Islemler
    #Donus degeri
#Yukaridaki fonksiyonu calistirmak icin:
#Fonksiyon_Adi() yazilir.   

def selamla():
    print('Merhaba')
    print('Nasilsiniz?')

selamla()

#Parametreler ve Argumanlar

def selamla2(isim):
    print('Isminiz:', isim)
selamla2('Berzah')

def toplama(a,b,c):
    print('Toplamlari:',a+b+c)

toplama(3,4,5)

def faktoriyel(sayi):
    faktoriyel = 1
    if (sayi==0 or sayi==1):
        print('Faktoriyel:',faktoriyel)

    else:
        while (sayi>=1):
            faktoriyel*=sayi
            sayi -=1
        print('Faktoriyel',faktoriyel)

faktoriyel(5)

#fonksiyonlarda Return

def toplama2(a,b,c):
    return a+b+c

def ikiylecarp(a):
    return 2*a

def dordebol(a):
    return a/4

toplam = toplama2(1,2,3)
print(dordebol(ikiylecarp(toplam)))


#Fonksiyonun icine default degerler atanabilir.
def selamla3(isim='isimsiz'):
    print('Selam:', isim)

selamla3()


def bilgilerigoster(ad='Bilgi Yok',soyad='Bilgi Yok',numara='Bilgi Yok'):
    print('Adi:',ad,'\nSoyadi:', soyad,'\nNumarasi:',numara)

bilgilerigoster(numara=55)

def toplama3(*a):
    toplamm=0
    for i in a:
        toplamm+=i
    return toplamm

print(toplama3(1,2,3))


liste = [1,2,3,4,5]
liste2=[i*2 for i in liste]
print(liste2)


#Lambda islemlerinde fonksiyon su sekilde olusturulur.
#Fonksiyon_Adi = lambda Parametre1, Parametre2,... : Islem
#Islem degeri return ile geri getirilir.

ucebolme = lambda x : x/3

print(ucebolme(5))


