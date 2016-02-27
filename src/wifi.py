WifiName='mexidron'
from wifi import Cell, Scheme
ap_list=Cell.all('wlan0')
for item in ap_list:
    if(item.ssid.find(WifiName) == 0):
        scheme = Scheme.for_cell('wlan0',WifiName, ap_list)
        scheme.save()
        scheme.activate()

