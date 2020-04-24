# Snake Tutorial Python
import matplotlib.pyplot as plt
import pygame
from bluepy.btle import Scanner
beacons_loc = [[19,70,'addr1',(255,165,0)], #orange
               [19,166,'01:02:03:04:05:f6:',(255,69,0)], #orangered
               [420,160,'38:18:4c:23:3f:f7',(255,215,0)]] # gold  / darkorange = 255,140,0 ; dark blue = 2,40,104

wall_locn = [[(19,70),(409,70)],[(420,166),(409,70)], [(19,166),(19,60)],[(19,166),(417,166)],
            [(116,355),(144,737)], [(144,737),(306,657)], [(306,657),(306,347)], [(116,355),(306,347)]]

scanner = Scanner()
f = open("location_07.txt","w+")
class beacon():
    rows = 20
    w = 500
    def __init__(self,x,y, addr, rssi=0, color=(0, 0, 204,255),color_b = (255,0,0,0),distance =0):
        print(x,y,addr)
        self.pos = (x,y)
        self.color = color
        self.color_b = color_b
        self.addr = addr
        self.rssi = rssi
        self.distance = distance
        beacons.append(self)
        beacon_addr.append(addr)
        self.rad = ((distance)*400/15)

    def draw(self, surface):
        global brick
        i = self.pos[0]
        j = self.pos[1]
       # print(self.rad)
        x=0
        pygame.draw.rect(surface, self.color_b, (i, j, brick ,brick ))
       # print("going to: ",self.pos,self.rad,x,self.distance)
        if abs(self.rssi) < 10:
            rad = 10
            x=0
        else: x,rad= 2, int(abs(self.rssi))
        pygame.draw.circle(surface,self.color,self.pos,rad,x)
          #self.rssi, self.rssi))
       


class target(object): # draw , pass = addr,|rssi|,pos,color

    def __init__(self, addr, rssi, r_pos, color=(0,255, 0)):
       # print(r_pos)
        self.r_pos = r_pos
        self.color = color
        self.addr = addr
        self.rssi = abs(rssi)
        self.pos = (r_pos)
        tar_addr.append(addr)
        targets.append(self)

    def draw(self, surface):
        #i =self.pos
        print("drawing target circle",self.addr)
        x=4
        if self.rssi <4:
            x=0
        pygame.draw.circle(surface,(0,255,0),(200,200),self.rssi,x)

class wall():   # pas: start.pos,stop.pos, brick_size, surface === now just drawing

    def __init__(self,start, end):
        self.start = start
        self.end = end
        print("wall: ",start," | ",end)
        walls.append(self)

    def draw(self,surface):
        pygame.draw.line(surface, (0, 0, 0), self.start, self.end, 5)



def drawGrid(rows,w,brick, surface):
    x = 0
    y = 0
    for l in range(rows):
        x = x + brick
        y = y + brick
        pygame.draw.line(surface, (220, 210, 200), (x, 0), (x, w))
        pygame.draw.line(surface, (200, 210, 220), (0, y), (w, y))


def redrawWindow(rows,width,surface):
    surface.fill((255, 255, 255))
    drawGrid(rows,width,brick, surface)
    for w in walls:
        w.draw(surface)
    for t in targets:
        t.draw(surface)
    for b in beacons:
        b.draw(surface)

    pygame.display.update()


def get_targets(devices):
    for device in devices:
        addre = device.addr
       # print("chheck here: ",addre)
        #38:18:4C:23:3F:F7            
        if(addre in beacon_addr):
            got = beacon_addr.index(addre)
            rssi = (device.rssi)
            #############################
            txPower = -59
            if (rssi == 0):
                distance =  (-1.0)
                continue

            ratio = rssi * 1.0 / txPower
            if (ratio < 1.0):
                distance = (ratio ** 10)
            else:
                distance =( (0.89976) * (ratio ** 7.7095) + 0.111)
            ##############################################
            print("got in for: ",addre," with rssi:",rssi,distance)
            rssi_l.append(rssi)
            dis_l.append(distance *100)
            distance = float(distance)
           # f.write(("Addr: "+str(addre)+" RSSI: "+str(rssi)+" Distance: "+str(distance)+"\n"))
            f.write(str(rssi) + ":"+str(distance)+ "\n")
            beacons[got].rssi, beacons[got].distance = -rssi ,distance
              

def main():
    global walls, brick,tar_addr,targets,beacons,rssi_l,dis_l,beacon_addr
    width = 800
    rows = 60
    brick = width // rows
    win = pygame.display.set_mode((width, width))
    flag = 0
    clock = pygame.time.Clock()
    targets = []
    tar_addr = []
    beacons = []
    beacon_addr = []
    walls = []
    #t = target("38:18:4c:23:3f:f7",0, 0)
    dis_l=[]
    rssi_l = []
    for w in wall_locn :
        wall(w[0],w[1])
    for b in beacons_loc:
        beacon(b[0],b[1],b[2],color_b = b[3])

    while (flag < 1000):
     #   pygame.time.delay(5)
        clock.tick(1)
        raw_devices = scanner.scan(0.01)
        get_targets(raw_devices)
        redrawWindow(rows,width,win)
        flag += 1
    print("While ends here ------- ",flag,len(rssi_l))   ##################while ends heree
    
main()
x = range(0,len(rssi_l))

f.close()
plt.plot(x,rssi_l,label = "RSSI")
plt.plot(x,dis_l,label="Distance")
plt.legend()
plt.show()
print("number of targets: ",len(targets))
