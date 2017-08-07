import sensor, image, time
from pyb import UART

#define
#Lab(Lmin,Lmax,Amin,Amax,Bmin,Bmax)
A4Black = [(0, 20, -10, 10, -5, 10)]
A4White = [(90,100,-10,10,-5,5)]
A4Red = [(60,75,-20,60,-10,10)]
Black = [(15,35,-10,20,-30,0)]
White = [(90,100,-10,10,-10,10)]
#thresholds = [A4Black,A4White,A4Red]
MID_POINT = [160,120]

def InitColorTrace():
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.skip_frames(time = 2000)
    sensor.set_auto_gain(False) # must be turned off for color tracking
    sensor.set_auto_whitebal(False) # must be turned off for color tracking

def BlobX(x):
    return x[0]

def BlobY(x):
    return x[1]

def BlobL(x):
    return x[2]

def BlobW(x):
    return x[3]

def BlobMid(x):
    return x[4]

def BlobPix(x):
    return x[5]

def BlobPos(x):
    Dict = {}
    Dict['LU']=[x[0],x[1]]
    Dict['LB']=[x[0],x[1]-x[2]]
    Dict['RU']=[x[0]+x[3],x[1]]
    Dict['RB']=[x[0]+x[3],x[1]-x[2]]
    Dict['MID']=[x[0]+int(x[3]/2),x[1]-int(x[2]/2)]
    Dict['Flag']=1
    return Dict

def ReturnStr(x):
    if len(x)<2:
        x = '000'+x
        return x
    elif len(x)<3:
        x = '00'+x
        return x
    elif len(x)<4:
        x = '0'+x
        return x
    else:
        return x[-4:]

def ANO_Send_Speed_S(param):
    send_str = 'aaaa0b02'

    x = ReturnStr(str(hex(param[0]).replace('x','')))
    send_str = send_str + x
    y = ReturnStr(str(hex(param[1]).replace('x','')))
    send_str = send_str + y
    _sum = ReturnStr(str(hex(353+param[0]+param[1]).replace('x','')))
    send_str = send_str + _sum
    print(send_str)
    return send_str


#def FindBall(img,param):
    #for blob in img.find_blobs(param,pixels_threshold=200,area_threshold=200):
        #if BlobW(blob)*BlobL(blob)<=1200 and BlobW(blob)*BlobL(blob)>=500:
            #img.draw_rectangle(blob.rect())
            #img.draw_cross(blob.cx(),blob.cy())
            #_dict = BlobPos(blob)
            #print("LR:(%d,%d) "%(_dict['LU'][0],_dict['LU'][1]))
            #print(_dict['MID'])
            ##uart.write(str(_dict['MID'][0]))
            #a=_dict['MID']
            #ANO_Send_Speed_S(a)
            #uart.write(ANO_Send_Speed_S(a))

def FindBall(img,param):
    for blob in img.find_blobs(param,pixels_threshold=200,area_threshold=200):
        if BlobW(blob)*BlobL(blob)<=1200 and BlobW(blob)*BlobL(blob)>=500:
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(),blob.cy())
            _dict = BlobPos(blob)
            a=_dict['MID']
            return ANO_Send_Speed_S(a)
  

def FindBlackArea(img):
    for blob in img.find_blobs(A4Black,pixels_threshold=10000,area_threshold=10000):
        if BlobW(blob)*BlobL(blob)<=50000:
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(),blob.cy())
            #print('BlackArea: ',BlobPos(blob))

def FindBlackAreaForCraft(img):
    for blob in img.find_blobs(Black,pixels_threshold=200,area_threshold=200):
        if BlobW(blob)*BlobL(blob)<=5000:
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(),blob.cy())
            return BlobPos(blob)
    _dict = {}
    _dict['Flag']=0
    return _dict

def FindWhiteAreaForCraft(img):
    for blob in img.find_blobs(White,pixels_threshold=200,area_threshold=200):
        if BlobW(blob)*BlobL(blob)<=5000:
            img.draw_rectangle(blob.rect())
            img.draw_cross(BlobX(blob),BlobY(blob))
            #return BlobPos(blob)
    _dict = {}
    _dict['Flag']=0
    return _dict

def FindRedCorner(img):
    for blob in img.find_blobs(A4Red,pixels_threshold=50,area_threshold=50):
        if BlobW(blob)*BlobL(blob)<=200:
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(),blob.cy())
            return BlobPos(blob)
    _dict = {}
    _dict['Flag']=0
    return _dict


def FindCorner1(img):
    c1 = [0,0,0]
    c2 = [0,0,0]
    c3 = [0,0,0]
    c4 = [0,0,0]
    for blob in img.find_blobs(White,pixels_threshold=50,area_threshold=50):
        if BlobW(blob)*BlobL(blob)<=800:
            img.draw_cross(BlobX(blob),BlobY(blob))
            #print('%d,%d\n' % (blob.cx(),blob.cy()))
            count = 0            
            if blob.cx()<=100 and blob.cy()<=30:
                c1[0]=blob.cx()
                c1[1]=blob.cy()
                c1[2]=1
                print(1)
                #print('Find C1 (%d,%d)\n'%(c1[0],c1[1]))
            if blob.cx()>=230 and blob.cy()<=30:
                c2[0]=blob.cx()
                c2[1]=blob.cy()
                c2[2]=1
                print(2)
                #print('Find C2 (%d,%d)\n'%(blob.cx(),blob.cy()))
            if blob.cx()>=230 and blob.cy()>=190:
                c3[0]=blob.cx()
                c3[1]=blob.cy()
                c3[2]=1
                print(3)
                #print('Find C3 (%d,%d)\n'%(blob.cx(),blob.cy()))
            if blob.cx()<=100 and blob.cy()>=190:
                c4[0]=blob.cx()
                c4[1]=blob.cy()
                c4[2]=1
                print(4)
                #print('Find C4 (%d,%d)\n'%(blob.cx(),blob.cy()))
            if blob.cx()>100 and blob.cx()<230 and blob.cy()>30 and blob.cy()<190:
                img.draw_rectangle(blob.rect())
                print('FindBall')
            flag = c1[2]+c2[2]+c3[2]+c4[2]
            #print(flag)
            if flag==4:
                p_x = int((int((c1[0]+c2[0])/2)+int((c3[0]+c4[0])/2))/2)
                p_y = int((int((c1[1]+c2[1])/2)+int((c3[1]+c4[1])/2))/2)
                print('PHY_MID:(%d,%d)\n'%(p_x,p_y))
                img.draw_cross(p_x,p_y)
            
                
InitColorTrace()
clock = time.clock()
uart = UART(3, 115200)
while(True):
    clock.tick()
    img = sensor.snapshot()
    FindCorner1(img)
