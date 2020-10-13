
def target_calculator(t):
    nbits = t
    hexnbytes = hex((nbits>>24) & 0xff)
    hexprefix = str(hex(nbits & 0xffffff))

    nbytes = int(hexnbytes,16) * 2 
    remaining_hex = nbytes - 6

    zeros = "0" * remaining_hex
    newprefix = hexprefix + zeros
    target = int(newprefix, 16)
    return target

#Target
newtarget = target_calculator(0x1729ff38)

#sTarget
starget = target_calculator(0x1d00ffff)


difficulty = starget/newtarget

print('Difficulty: ', str(difficulty))

