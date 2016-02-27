WifiName='sanjurjo'
WifiPassword='None'
NotFound=True
from wifi import Cell, Scheme
while (NotFound):
    ap_list=Cell.all('wlan0')
    for item in ap_list:
        if(item.ssid.find(WifiName) == 0):
            print item
            NotFound=False
            scheme.delete()
            scheme = Scheme.for_cell('wlan0',WifiName,item,passkey=WifiPassword)
            scheme.save()
    scheme.activate()