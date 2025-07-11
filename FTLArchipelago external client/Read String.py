from operator import concat
import pymem
import pymem.process
import struct
def Decode(ints: list[int]) -> str:
    chars = []
    for number in ints:
        if 0 < number <= 127:  # Only allow valid ASCII
            chars.append(chr(number))
        elif number == 0:
            chars.append('#') # visualize null characters
        else:
            chars.append('-')  # visualize garbage characters
    return ''.join(chars)

# encode and decode (internal numeric representation)? <-> string
def Encode(string: str) -> list[int]:
    ints = []
    for char in string:
        ints.append(ord(char))
    return ints

pm = pymem.Pymem("FTLGame.exe")

address = 502700488

data = pm.read_bytes(address, 1024 * 4)

ints = [int(byte) for byte in data]

print(Decode(ints))