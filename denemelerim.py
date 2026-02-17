import sys
kf_ch4= float(input("ch4 kütle fraksiyonunu giriniz:"  ))
kf_c3h8 = float(input("c3h8  kütle fraksiyonunu giriniz :  "))
kf_h2 = float(input("h2  kütle fraksiyonunu giriniz:  "))

toplam_fraks = kf_ch4 + kf_c3h8 + kf_h2

if toplam_fraks != 1:
    print("toplam kütle fraksiyonu 1 olmalıdır!")
    sys.exit()

x_karisim_kutlesi = 100.0 ##assumption (mol or kmol)
M_agirligi_ch4 = 16.04
M_agirligi_c3h8 = 44.10
M_agirligi_h2 = 2.016
M_agirligi_o2 = 32.0
M_agirligi_n2 = 28.01
M_agirligi_h2o = 18.02
M_agirligi_co2 = 44.01
def toplam_kutle_mol_sayilarina_gecis(kf_ch4 , kf_c3h8 , kf_h2):
    m_ch4 = kf_ch4 * x_karisim_kutlesi
    m_c3h8 = kf_c3h8 * x_karisim_kutlesi
    m_h2 = kf_h2 * x_karisim_kutlesi

    n_mol_ch4 = (m_ch4 / M_agirligi_ch4)
    n_mol_c3h8 = (m_c3h8 / M_agirligi_c3h8)
    n_mol_h2 = (m_h2 / M_agirligi_h2)

    return n_mol_h2, n_mol_c3h8, n_mol_ch4

n_h2_end, n_c3h8_end, n_ch4_end = toplam_kutle_mol_sayilarina_gecis(kf_h2 , kf_c3h8 , kf_ch4)

toplam_oksijen = (n_ch4_end * 2 ) + (n_c3h8_end * 5) + (n_h2_end / 2)
beslenen_oksijen = toplam_oksijen * 1.2
#URUNLER#
n_mol_co2 = (n_ch4_end + (3* n_c3h8_end))
n_mol_h2o = ((2*n_ch4_end) + (4*n_c3h8_end) +n_h2_end)
n_mol_N2 = beslenen_oksijen * 0.79
n_mol_o2 = beslenen_oksijen - toplam_oksijen

m_o2 = n_mol_o2 * M_agirligi_o2
m_n2 = n_mol_N2* M_agirligi_n2
m_co2= n_mol_co2 * M_agirligi_co2
m_h2o = n_mol_h2o* M_agirligi_h2o
###baca gazı kütle fraksiyonları
x_karisim_urunler = m_co2 + m_h2o + m_n2 + m_o2
x_co2_kutle = m_co2 / x_karisim_urunler
x_h2o_kutle = m_h2o / x_karisim_urunler


print("CO2 'in kütle fraksiyonu" , x_co2_kutle )
print("H2O 'nun kütle fraksiyonu", x_h2o_kutle)



