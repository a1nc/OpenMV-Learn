def ANO_Send_Speed(param):
    send_str = 'AAAA0B02'
    x = str(hex(param[0]).replace('x','').zfill(2))[-2:]
    send_str = send_str + x
    y = str(hex(param[1]).replace('x','').zfill(2))[-2:]
    send_str = send_str + y
    sum = str(hex(353+param[0]+param[1]).replace('x','').zfill(2))[-2:]
    send_str = send_str + sum
    print(send_str)
    return send_str
    
    
def ANO_Send_Speed_S(param):
    send_str = 'AAAA0B02'
    x = str(hex(param[0]).replace('x',''))
    if len(x)<2:
        x = '0' + x
    else:
        x = x[-2:]
    send_str = send_str + x
    y = str(hex(param[1]).replace('x',''))
    if len(y)<2:
        y = '0' + y
    else:
        y = y[-2:]
    send_str = send_str + y
    sum = str(hex(353+param[0]+param[1]).replace('x',''))
    if len(sum)<2:
        sum = '0' + sum
    else:
        sum = sum[-2:]
    send_str = send_str + sum
    print(send_str)
    return send_str


a = [33,50]
ANO_Send_Speed(a)
# uart.write(ANO_Send_Speed(a))
