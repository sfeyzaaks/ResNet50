## n(yeni) = n(eski) - f(n)/f'(n)
import numpy as np 

def f(n):
    return (n**3 - 4.605263158 * n ** 2 + 12.0279809 * n - 9.781089893) #van der waals hal denkleminden çıkardığımız sonuç

def f_prime(n): 
    return 3 * n ** 2 - 0.57516 * n + 0.31126

max_iterasyon = 10 #max iterasyon denemesi
M_su = 18.015 #kg/kmol

n_eski  = (60000 * 0.14) / (8.3144 * 1023) #ideal yasadan ideal gazın molü bulunur. başlangıç değeri
 
iterasyon_sayisi = 0 
print("başlangıç tahmini:" , n_eski)

while iterasyon_sayisi < max_iterasyon :
    f_n = f(n_eski)
    f_prime_n = f_prime(n_eski)
    

    if np.abs(f_prime_n) < 1e-10 :
        print("hata: türev sıfıra yaklaştı.")
        break
    n_yeni = n_eski - (f_n / f_prime_n)

    bagil_hata =np.abs((n_yeni - n_eski)/ n_yeni)
    print(f"iterasyon sayısı {iterasyon_sayisi + 1} : n= {n_yeni : .5f} kmol , Hata: {bagil_hata : .8f}")
    n_eski = n_yeni
    iterasyon_sayisi += 1 

else:
    print(f"Tanımlanan {max_iterasyon} sayısı tamamlandı.")

n_son = n_yeni
m_son = n_son * M_su 

print(f"\n sonuçlar:")
print(f"kütle (m) : {m_son}") #kg












