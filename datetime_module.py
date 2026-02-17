
# # import datetime
# from datetime import datetime
# from datetime import timedelta
# sonuc = dir(datetime) #içerisinde neler olduğu hakkında bilgi verir
# simdi = datetime.now() #bugünün tarihi
# simdi = datetime.today()
# sonuc = datetime.now()
# sonuc = simdi.year
# sonuc = simdi.month
# sonuc = datetime.ctime(simdi) #zamanı yazılı şekilde verir
# sonuc = datetime.strftime(simdi,"%Y") #yalnızca yılı verir
# sonuc = datetime.strftime(simdi,"%X") #saati verir
# sonuc = datetime.strftime(simdi,"%d") #günü verir sayı olaral
# sonuc = datetime.strftime(simdi,"%A") #günü verir yazı olarak
# birthday = datetime(1990,6,24,7,30,59)
# sonuc = datetime.timestamp(birthday) #saniye cinsinden verir 
# sonuc = simdi - birthday
# sonuc = sonuc.seconds
# sonuc = simdi + timedelta(10) #simdi ye 10 gün ekledi
# sonuc = simdi + timedelta(days=500,minutes = 20) # 500 gün + 20 dskika ilerledi




###############
#now ver,now sadece year,ctime,strftime YXdA,birthday yazdır,timestamp,timedelta

import datetime
from time import datetime
from time import timedelta
sonuc = dir(datetime)
simdi = datetime.now()
print(sonuc)


