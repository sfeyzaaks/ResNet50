import numpy as np
import matplotlib.pyplot as plt

# --- 1. Veriler ---
K = 16.99
# Basınç değerlerini liste olarak tanımlıyoruz
P_values = [10, 15, 20, 25, 30]

# --- 2. İdeal Gaz Hesaplaması ---
# K = y_iso / y_n  ve  y_iso + y_n = 1 denklemlerinden:
y_iso_degeri = K / (1 + K)  # Yaklaşık 0.9444
y_n_degeri = 1 - y_iso_degeri # Yaklaşık 0.0556

# Her basınç noktası için aynı mol kesri değerini içeren listeler oluşturuyoruz
# (Boyut hatası -error- almamak için liste boyutu P_values ile aynı olmalı)
y_iso_plot = [y_iso_degeri for _ in P_values]
y_n_plot = [y_n_degeri for _ in P_values]

# --- 3. Grafik Çizimi ---
plt.figure(figsize=(8, 5))

# n-Bütan çizgisini çizdir
plt.plot(P_values, y_n_plot, 'bo-', label='n-Bütan (n-C4H10)', linewidth=2)
# iso-Bütan çizgisini çizdir
plt.plot(P_values, y_iso_plot, 'ro-', label='izo-Bütan (iso-C4H10)', linewidth=2)

# Grafik düzenlemeleri
plt.title(f'A Şıkkı: İdeal Gaz Denge Bileşimi (K = {K})')
plt.xlabel('Basınç (bar)')
plt.ylabel('Mol Kesri (y_i)')
plt.ylim(0, 1.05) # Y eksenini 0 ile 1 arasında sınırla
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='best')

plt.show()

# --- 4. Tablo Çıktısı ---
print(f"{'Basınç (bar)':<15} {'y_n (n-C4H10)':<15} {'y_iso (iso-C4H10)':<15}")
print("-" * 45)
for i in range(len(P_values)):
    print(f"{P_values[i]:<15} {y_n_plot[i]:<15.4f} {y_iso_plot[i]:<15.4f}")