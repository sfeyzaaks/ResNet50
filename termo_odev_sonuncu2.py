import numpy as np
import matplotlib.pyplot as plt

K_sabit = 1.644
P_degerleri = np.array([10, 15, 20, 25, 30])
T = 425.0
# Kritik Değerler
tc_n, pc_n = 425.1, 37.96 
tc_i, pc_i = 408.1, 36.48

def phi_rk_hesapla(T, P, Tc, Pc):
    R = 0.08314
    Tr, Pr = T/Tc, P/Pc
    A2 = 0.42748 * Pr / (Tr**2.5)
    B = 0.08664 * Pr / Tr
    Z = 1 + B - A2 * B / (1 + B) # Gaz fazı yaklaşımı
    ln_phi = (Z-1) - np.log(Z-B) - (A2/B) * np.log(1 + B/Z)
    return np.exp(ln_phi)

y_iso_list = []
for P in P_degerleri:
    phi_iso = phi_rk_hesapla(T, P, tc_i, pc_i)
    phi_n = phi_rk_hesapla(T, P, tc_n, pc_n)
    Ky = phi_iso / phi_n
    # K = (y_iso/y_n) * Ky  => y_iso = (K/Ky) / (1 + K/Ky)
    K_eff = K_sabit / Ky
    y_iso_list.append(K_eff / (1 + K_eff))

# --- Grafik Çizimi ---
plt.figure(figsize=(8, 5))
plt.plot(P_degerleri, y_iso_list, 'ro-', label='iso-Bütan (RK - B Şıkkı)')
plt.plot(P_degerleri, 1 - np.array(y_iso_list), 'bo-', label='n-Bütan (RK - B Şıkkı)')

plt.title('B Şıkkı: RK Modeline Göre Hassas P-yi Grafiği')
plt.xlabel('Basınç (bar)')
plt.ylabel('Mol Kesri (y_i)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

# Hassas Tabloyu Yazdır (Eğimi görmek için)
print(f"{'P':<5} {'y_iso':<10}")
for i in range(len(P_degerleri)):
    print(f"{P_degerleri[i]:<5} {y_iso_list[i]:.6f}")

# Önemli: Eğim çok küçük olacağı için ekseni daraltarak değişimi görebilirsin
# plt.ylim(0.94, 0.95) # Eğer iso-bütandaki eğimi görmek istersen bunu açabilirsin.

plt.show()