import numpy as np



r = float(input("geri dönüm oranını giriniz: "))#geri dönüm oranı
e = float(input("ayırma verimini giriniz: "))#ayırma verimi
if r>= 1 or e >= 1:
    raise SystemError("oranlar 1 den küçük olmalıdır.")
    
F1 = 100
F3 = 60
F5 = 40
F4 = 40 / (1 - r)
F6 = F4 - 40
F2 = F1 + F6

x_b_2 = float(25 / (F2- ((F6*e*F2 )/ 40)))
x_b_5 = float((F2*x_b_2*e)/ F5)

concentration_matrix = np.array([[F2, x_b_2],
                                 [F5, x_b_5]])
tutarli= False
if 0.20 < x_b_2 <= 0.25:
    if 0.4< e<= 0.5: tutarli = True
    beklenen = "0.20< xB2 <=0.25 ve 0.4<ayırma verimi<=0.5"
elif 0.25 < x_b_2 <=0.28:
    if 0.5 < e <= 0.6: tutarli = True
    beklenen = "0.25< xB2 <=0.28 ve 0.5<ayırma verimi<=0.6"
elif 0.28 < x_b_2 <=0.30:
    if 0.6 < e <= 0.7: tutarli = True
    beklenen = "0.28< xB2 <=0.30 ve 0.6<ayırma verimi<=0.7"
elif 0.30 < x_b_2 <=0.40:
    if 0.7 < e <= 0.8: tutarli = True
    beklenen = "0.30< xB2 <=0.40 ve 0.7< ayırma verimi<=0.8"
else:
    beklenen = "Tablo dışı xB2 değerleri"
if tutarli:
    print("girilen değerler tutarlıdır.")
    print("konsantrasyon matrisi: \n ", concentration_matrix)
else:
    print("girdiğiniz değerler tutarsızdır. Beklenen aralıklar:",beklenen )

