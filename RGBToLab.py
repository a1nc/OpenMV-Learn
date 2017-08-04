def gamma(x):
    if 0.04045 < x:
        return pow((x+0.055)/1.055, 2.4)
    else:
        return x/12.92


def RGBToLab(r, g, b):
    R = gamma(r/255.0)
    G = gamma(g/255.0)
    B = gamma(b/255.0)

    x = 0.412453*R+0.357580*G+0.180423*B
    y = 0.212671*R+0.715160*G+0.072169*B
    z = 0.019334*R+0.119193*G+0.950227*B

    x = x/0.95047
    y = y/1.0
    z = z/1.08883

    FX = FY = FZ = 0
    if x>0.008856:
        FX = pow(x,1.0/3.0)
    else:
        FX = 7.787*x+0.137931

    if y>0.008856:
        FY = pow(y,1.0/3.0)
    else:
        FY = 7.787*y+0.137931

    if z>0.008856:
        FZ = pow(z,1.0/3.0)
    else:
        FZ = 7.787*z+0.137931

    lab = {}
    if y>0.008856:
        lab['L'] = 116.0*FY-16.0
    else:
        lab['L'] = 903.3*y
    lab['A'] = 500.0*(FX-FY)
    lab['B'] = 200.0*(FY-FZ)
    return lab

print(RGBToLab(255,255,255))
print(RGBToLab(255,0,138))
print(RGBToLab(255,63,0))
print(RGBToLab(0,255,253))
print(RGBToLab(182,0,255))
