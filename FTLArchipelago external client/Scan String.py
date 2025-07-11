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
            continue  # skip garbage or uninitialized values
    return ''.join(chars)

# encode and decode (internal numeric representation)? <-> string
def Encode(string: str) -> list[int]:
    ints = []
    for char in string:
        ints.append(ord(char))
    return ints

pm = pymem.Pymem("FTLGame.exe")

ints = Encode("Started new run")

hexes = [hex(i) for i in ints]

hex_string = ''.join(h[2:] for h in hexes)

pattern = bytes.fromhex(hex_string)

addresses = pm.pattern_scan_all(pattern, return_multiple=True)

print(addresses)

for address in addresses:
    data = pm.read_bytes(address, 1024 * 4)
    ints = [int(byte) for byte in data]
    print(f"{address}\n{Decode(ints)}\n\n")