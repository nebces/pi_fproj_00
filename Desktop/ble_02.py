from bluepy.btle import Scanner
from Tkinter import *
 
scanner = Scanner()


'''def create_circle(x,y,r,c_n):
    x0 = x-r
    y0 = y-r
    x1 = x+r
    y1 = y+r
    return c_n.create_oval(x0, y0, x1, y1)



root = Tk()
root.title('gui working')
root.geometry('600x600')
myc = Canvas(root,height = 600,width = 600,bg ='white')
myc = Canvas(root)
myc.pack()
create_circle(100, 100, 20, myc)'''
#button = Button(root,text = 'stop', width = 25 )
#button.pack()
#root.mainloop()

while(1):
    devices = scanner.scan(10.0)
     
    for device in devices:
        print("DEV = {}RSSI = {}".format(device.addr, device.rssi))
        #print(type(device))
        rssi = device.rssi
        
        txPower = -59
        if (rssi == 0 ):
            print(-1.0)
        
        ratio = rssi * 1.0 / txPower
        if (ratio < 1.0):
            distance = (ratio ** 10)
        else:
            distance = (0.89976)*(ratio**7.7095) + 0.111
        print(distance)
        #create_circle(100, 100, distance*10, myc)

#arc = c.create_arc(10,50,240,210, extent = 150, fill= 'red')
#c.pack
root.mainloop()






