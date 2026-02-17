
P= 1.5 #atm
R = 0.08206 #L.atm/mol.K
V = 150 #L/s
T_1 = 150 + 273.15 #kelvin
n_0 = ((P*V) /(R*T_1)) #mol/s

n_0_aseton = (((0.875/58.08) *150 )/ 2.5)  #2.5 L için 0.875gr aseton miktarı yoğuşmuşsa 150 L için ne kadar yoğuşur bulduk
n_0_hava = n_0 - n_0_aseton

T_2 =  -18  # sıcaklık (derece Celcius)
psat = 10 ** (7.117 - (1210.595 / T_2 + 229.664)) #asetonun -18 derecede doygun buhar basıncı(mmhg), antoine eşitliğinden
y_1_aseton = psat / (4.5 * 760)

n_1_hava = n_0_hava
n_1_aseton = n_1_hava * (y_1_aseton / (1 - y_1_aseton))

n_2_aseton = n_0_aseton + n_1_aseton

H_0_aseton = 48.1
H_0_hava = 3.666
H_1_aseton = 34.0
H_1_hava = -1.245
H_2 = 0

H_toplam = ((H_1_aseton * n_1_aseton)+ (H_1_hava * n_1_hava) + (H_2 * n_2_aseton) - (H_0_aseton * n_0_aseton) - (H_0_hava * n_0_hava))
W = -22 #kj/s
Q = H_toplam + W #kj/s
print("mol sayıları :" , "n0:", n_0, "n_1:" ,n_1_aseton + n_1_hava, "n_2:", n_2_aseton)
print("Isı değişimi (Q):", Q) 
