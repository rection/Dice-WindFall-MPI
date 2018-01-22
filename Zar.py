#!/bin/python
#SAFA BAYAR  Ogrenci No: 161906001
#calistirmak icin: 'mpiexec -n 4 python Zar.py '
from random import randint		
from mpi4py import MPI			 #Kutuphane tanimlamalari
import numpy

comm = MPI.COMM_WORLD
rank = comm.rank			#Paralellestirmek icin kutuphanedekileri degisken olarak ataniyor.
size = comm.Get_size()
sum = 0

def donguler():				#donguler adinda fonksiyon tanimlamasi 
     cnt = 0				#degisken tanimlamasi ve sifirlamasi
     for var in range (1,1000):		#1000 tane zar atilmakta
        l = randint(0,6)		#l degiskenine  0 ile 6 arasinda rastgele deger atanmaktadir. Zarin uzerinde ki sayiyi ifade etmektedir.
        m = randint(0,6)		#k degiskenine  0 ile 6 arasinda rastgele deger atanmaktadir. Zarin uzerinde ki sayiyi ifade etmektedir.
        if l == m & l == 6 & m == 6:	#Onemli bir satir. l ve m 0 ile 6 arasinda herhangi atilmis degeri ifade etmektedir.Gelen degerin birbirine esit olma durumu 
					#1.sart, l'nin 6'ya esit olma durumu ikinci sart, m'nin 6'ya esit olma durumu 3.sarttir. & ve operatorudur.
            print l , '  ' , m		#kosulu saglayan degerler bastirilmaktadir.

            cnt +=1			#sayac tutulmasi amaci kac tane oldugunu bulmaktir.
            print cnt			#Kac tane oldugu bastirilmaktadir.
     return None			#Fonksiyon null dondurmesi icin





if rank == 0:					#sifirinci  yani main cekirdek atatigimiz degere gelince asagidakini uygula anlamina geliyor. 
    sum = donguler()				#fonksiyonu degiskene atiyoruz. mpi'da parametre olarak fonksiyon kullanamamaktayiz. 
    for i in range(1,size):			#size degiskeni yukarda kac cekirdege sahip oldugumuzu gosterir.
        sum = comm.recv(source=i)		 #sum degeri butun cekirdeklere dagitilan islemin sonucudur.
 

else:
    sum = donguler()				#eger cekirdeklere dagitilmiyor ise sifirinci yani main cekirdekte islemin yapilmasini belirtmekte			
    comm.send(sum,dest=0)

