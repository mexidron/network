WifiName='mexidron'
WifiPassword='udooers00'
from wifi import Cell, Scheme
ap_list=Cell.all('wlan0')
for item in ap_list:
    if(item.ssid.find(WifiName) == 0):
        scheme.delete()
        scheme = Scheme.for_cell('wlan0',WifiName,item,passkey=WifiPassword)
        scheme.save()

scheme.activate()