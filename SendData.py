import sensor, image, time
from pyb import UART

#define
#Lab(Lmin,Lmax,Amin,Amax,Bmin,Bmax)
A4Black = [(0, 20, -10, 10, -5, 10)]
A4White = [(90,100,-10,10,-5,5)]
A4Red = [(40,65,40,65,0,25)]
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


#InitColorTrace()
#clock = time.clock()
#uart = UART(3, 115200)
#while(True):
    #clock.tick()
    #img = sensor.snapshot()
    #for blob in img.find_blobs(A4Red, pixels_threshold=200, area_threshold=200):
        ##FindBall(img,A4White)
        #uart.write(FindBall(img,A4Red))
        #FindBlackArea(img)

a = [125,125]
ANO_Send_Speed_S(a)
