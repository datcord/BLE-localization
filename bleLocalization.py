import bluetoothScan
import bluetooth._bluetooth as bluez
import math
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import sys

if len(sys.argv) > 3:
    xreal = float(sys.argv[2])
    yreal = float(sys.argv[3])
    
c = -62.81
n = 1.642
dev_id = 0
x = 0.0
y = 0.0

try:
    sock = bluez.hci_open_dev(dev_id)
    print("\n *** Looking for BLE Beacons ***\n")
    print("\n *** Close figure to Cancel ***\n")
except BaseException:
    print("Error accessing bluetooth")

bluetoothScan.hci_enable_le_scan(sock)
# Scans for iBeacons
#e = distList[0]a
#g = distList[1]b
#f = distList[2]c
fig = pyplot.figure()
def animate(i):
    global x,y
    distList = [0.0, 0.0, 0.0]
    try:
        while True:
            returnedList = bluetoothScan.parse_events(sock, 10)
            for item in returnedList:
                if item["uuid"] == "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa":
                    distList[0] = pow(10,((c-item["rssi"])/(10*n)))
                if item["uuid"] == "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb":
                    distList[1] = pow(10,((c-item["rssi"])/(10*n)))
                if item["uuid"] == "cccccccc-cccc-cccc-cccc-cccccccccccc":
                    distList[2] = pow(10,((c-item["rssi"])/(10*n)))
            if distList[0] != 0.0 and distList[1] != 0.0 and distList[2] != 0.0:
                break
        e = distList[0]
        g = distList[1]
        f = distList[2]
        #math functions made for points C(1,0) and B(0,1)
        xtmp = (pow(e,2)-pow(f,2)+pow(g,2))/2
        ytmp = (pow(e,2)-pow(g,2)+1)/2
        if len(sys.argv) > 3:
            error = math.sqrt(pow((xtmp-xreal),2)+pow((ytmp-yreal),2))
            print("x:",xtmp,"y:",ytmp,"e:",error)
        else:
            print("x:",xtmp,"y:",ytmp)
        if i == int(sys.argv[1])-2:
            x += xtmp
            y += ytmp
            x = x/(i+1)
            y = y/(i+1)
            if x<10 and y<10:
                pyplot.clf()
                pyplot.plot(x,y,'bo',0,0,'bs',0,1,'bs',1,0,'bs')
                if len(sys.argv) > 3:
                    error = math.sqrt(pow((x-xreal),2)+pow((y-yreal),2))
                    print("AV: x:",x,"y:",y,"e:",error)
                else:
                    print("AV: x:",x,"y:",y)
        else:
            x += xtmp
            y += ytmp
        if i == int(sys.argv[1])-2:
            print()
            x = 0
            y = 0
        return x,y
    except KeyboardInterrupt:
        pass


anim = animation.FuncAnimation(fig,animate,int(sys.argv[1])-1)

pyplot.show()



