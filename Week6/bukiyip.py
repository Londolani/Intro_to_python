def bukiyip_to_decimal(a):
    if len(str(a)) == 1:
        return a
    else:
        return 3*int(str(a)[0]) + int(str(a)[1])

def decimal_to_bukiyip(a):
    if len(str(a)) == 1:
        if a < 3:
            return a
        else:
            return int('1' + str(a % 3))
    else:
        bukiyip_num = 0
        tenths = int(str(a)[0])*10
        units = int(str(a)[1])
        bukiyip_num = (tenths // 3)*10
        if units < 3:
            return bukiyip_num + units
        else:
            return bukiyip_num + 10 + units % 3

def bukiyip_add(a,b):
    return decimal_to_bukiyip(bukiyip_to_decimal(a) + bukiyip_to_decimal(b))

def bukiyip_multiply(a,b):
    return decimal_to_bukiyip(bukiyip_to_decimal(a)*bukiyip_to_decimal(b))
