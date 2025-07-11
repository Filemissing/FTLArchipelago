import pymem
import struct


def init_bridge():
    pass

def recieve_message():
    pass

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

pm = pymem.Pymem("FTLGame.exe")

vector_address = 0x23e536b0
data_ptr_bytes = pm.read_bytes(vector_address, 4)
userdata = struct.unpack("<i", data_ptr_bytes)  # '<Q' for little-endian unsigned long long
data_ptr = userdata[0]

print(f"Data pointer: {hex(data_ptr)}")

data_bytes = pm.read_bytes(data_ptr, 1024 * 4)  # 4 bytes per int
data = struct.unpack("<1024i", data_bytes)

print(Decode(data))