import sensor, image, time

#Lab(Lmin,Lmax,Amin,Amax,Bmin,Bmax)
A4Black = [(30, 65, -20, 5, -5, 25)]
A4White = [(90,100,-10,10,-5,15)]
A4Red = [(75,90,0,40,-20,5)]
#thresholds = [A4Black,A4White,A4Red]

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

def FindBall(img,param):
    for blob in img.find_blobs(param,pixels_threshold=200,area_threshold=200):
        if BlobW(blob)*BlobL(blob)<=1200:
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(),blob.cy())
            print('Ball: ',BlobPos(blob))

def FindBlackArea(img):
    for blob in img.find_blobs(A4Black,pixels_threshold=20000,area_threshold=20000):
        if BlobW(blob)*BlobL(blob)<=40000:
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(),blob.cy())
            print('BlackArea: ',BlobPos(blob))

InitColorTrace()
clock = time.clock()
while(True):
    clock.tick()
    img = sensor.snapshot()
    #for blob in img.find_blobs(thresholds, pixels_threshold=200, area_threshold=200):
    FindBall(img,A4White)
    FindBall(img,A4Red)
    FindBlackArea(img)
