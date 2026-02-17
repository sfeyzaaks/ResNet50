import sys
wch4= float(input("CH4 için kütle fraksiyonunu giriniz:"  ))
wc3h8 = float(input("C3H8 için kütle fraksiyonunu giriniz :  "))
wh2 = float(input("H2 için kütle fraksiyonunu giriniz:  "))

tot_fraks = wc3h8 + wch4 + wh2

if tot_fraks != 1:
    print("girilen değerler hatalıdır!")
    sys.exit()

x_karisim = 100.0 ##assumption (mol or kmol)
M_ch4 = 16.04
M_c3h8 = 44.10
M_h2 = 2.016
M_o2 = 32.0
M_n2 = 28.01
M_h2o = 18.02
M_co2 = 44.01
def toplam_kutle_mol_sayilarina_gecis(wch4 , wc3h8 , wh2):
    m_ch4 = wch4 * x_karisim
    m_c3h8 = wc3h8 * x_karisim
    m_h2 = wh2 * x_karisim

    n_ch4 = (m_ch4 / M_ch4)
    n_c3h8 = (m_c3h8 / M_c3h8)
    n_h2 = (m_h2 / M_h2)

    return n_h2, n_c3h8, n_ch4

n_h2_sonuc, n_c3h8_sonuc , n_ch4_sonuc = toplam_kutle_mol_sayilarina_gecis(wh2 , wc3h8 ,wch4)

tot_o2 = (n_ch4_sonuc * 2 ) + (n_c3h8_sonuc * 5) + (n_h2_sonuc / 2)
beslenen_o2 = tot_o2 * 1.2
###baca gazı ürünleri
def yanma_sonucu(n_ch4_sonuc,n_h2_sonuc,n_c3h8_sonuc):
    n_co2 = (n_ch4_sonuc + (3* n_c3h8_sonuc))
    n_h2o = ((2*n_ch4_sonuc) + (4*n_c3h8_sonuc) +n_h2_sonuc)
    n_N2 = beslenen_o2 * 0.79
    n_o2 = beslenen_o2 - tot_o2

    m_o2 = n_o2 * M_o2
    m_n2 = n_N2* M_n2
    m_co2= n_co2 * M_co2
    m_h2o = n_h2o* M_h2o

     ###kütle fraskiyonları
    x_karisim_urun = m_co2 + m_h2o + m_n2 + m_o2
    x_co2 = m_co2 / x_karisim_urun
    x_h2o = m_h2o / x_karisim_urun
    x_n2 = m_n2 / x_karisim_urun
    x_o2 = m_o2 / x_karisim_urun
    return x_co2 , x_h2o , x_n2 , x_o2

sonuc_urun = yanma_sonucu(n_c3h8_sonuc,n_ch4_sonuc,n_h2_sonuc)
print("  BACA GAZI KÜTLE FRAKSİYONLARI  ")
print("CO2 için kütle fraksiyonu: " , sonuc_urun[0])
print("H2O için kütle fraksiyonu: ", sonuc_urun[1])
print("N2 için kütle fraksiyonu: ", sonuc_urun[2])
print("O2 için kütle fraksiyonu: ", sonuc_urun[3])







