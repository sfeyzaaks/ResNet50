import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

P_boyler_mpa = [1500, 4800, 6000, 10000, 11400]
veri = { "P_boyler_mpa": P_boyler_mpa,
        "h1_kj/kg": [3472.8, 3435.9 , 3422.2 , 3374.6 , 3357.2],
        "h2_kj/kg": [2373.72, 2193.56, 2155.13, 2065.94, 2042.23],
        "h3_kj/kg": [175.8,175.8,175.8,175.8,175.8],
        "h4_kj/kg": [177.31,180.63,181.85,185.88,187.29]}
df = pd.DataFrame(veri)
W_net = 100000 #kj/s
w_net = df["h3_kj/kg"] - df["h4_kj/kg"]- (df["h2_kj/kg"] - df["h1_kj/kg"])

m_dot = W_net/ w_net
#1.grafik

plt.plot(df["P_boyler_mpa"], m_dot, marker = "o")
plt.title("Buhar türbininde Boyler basıncına karşı çalıştırıcı akışkan kütlesel hızı(kg/s)")
plt.show()

#2.grafik
Q_H_dot = m_dot * (df["h1_kj/kg"]- df["h4_kj/kg"])

plt.plot(P_boyler_mpa , Q_H_dot/1000 , marker = "o" , mec = "red")
plt.title("Boyler basıncına karşı çalıştırıcı akışkana olan ısı aktarım hızı(MW)")
plt.show()

#3.grafik
n = 1 - ( (df["h2_kj/kg"] - df["h3_kj/kg"])) / ((df["h1_kj/kg"] - df["h4_kj/kg"]))
plt.plot( P_boyler_mpa , n*100 , marker = "o", mec = "red")
plt.title("Boyler basıncına karşı çevrimin termal verimi (%)")
plt.show()
#4.grafik
Q_C_Ddot = m_dot * (df["h2_kj/kg"] - df["h3_kj/kg"])
plt.plot(P_boyler_mpa, Q_C_Ddot/1000 , marker = "o", mec ="red")
plt.title("Boyler basıncına karşı çalıştırıcı akışkandan olan ısı aktarım hızı (MW)")
plt.show()
