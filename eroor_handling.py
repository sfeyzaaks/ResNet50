# while True:
#     try:
#        a = int(input("a :"))
#        b = int(input("b :"))
#        print(a/b)
#     except ZeroDivisionError:
#       print("b sayısı 0 olamaz.")
#     except ValueError:
#       print("sadece sayısal veri giriniz.")
#     except Exception:
#       print("hata alındı")
#     else:
#         break

# while True:
#     try:
#        a = int(input("a :"))
#        b = int(input("b :"))
#        print(a/b)
#     except (ZeroDivisionError,ValueError) as e:  #programcı hatanın türünü verebilir bu şekilde
#       print("hata alındı.")
#       print(e)
    
#     except Exception:
#       print("bilinmeyen bir hata oluştu.")
#     else:
#         break #bunu yazdığımızda döngüyü başa alır yani tekrardan ekrana a yı yazar
#     finally:
#        print("finally bloğu çalıştı.") #hata olsa da olmasa da çalışır

##############
#döngüye sokmadan
#döngüye sokarak

# try:
#     a = int(input("sayı 1:"))
#     b = int(input("sayı 2:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("b sayısı 0 olamaz.")
    
# except ValueError:
#     print("lütfen sayı giriniz.")
# except Exception:
#     print("bir hata oluştu.")
while True:
    try:
        a = int(input("sayı 1:"))
        b = int(input("sayı 2:"))
        print(a/b)
    except ZeroDivisionError as e:
        print("b sayısı 0 olamaz.")
        print(e)
    except ValueError:
        print("lütfen sayı giriniz.")
    except Exception:
        print("bir hata oluştu.")
    else:
        break