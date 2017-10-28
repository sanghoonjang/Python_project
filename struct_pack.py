# struct module
# pack(format, v1, v2, v3, ...)
# unpack(format, string)
# calcsize(format)


from struct import *

"""
Format, C Type, Python, size
x, pad byte, novalue, 1
c, char, text of 1 langth, 1
b, signed char, a whole number, 1
B, unsigned char, a whole number, 1
h, short, a whole number, 2
H, unsigned short, a whole number, 2
i, int, a whole number, 4
I, unsigned int, a whole number, 4
l, long, a whole number, 4
L, unsigned long, a whole number, 4
f, float, float, 4
d, double, float, 8
s, char[], text, 1
p(small), char[], text, 1
P(dig), void, a whole number, 8
"""

# Change Data of Python To Binary data of C program
a = pack('hhh', 1,2,3)
a # b'\x01\x00\x02\x00\x03\x00'
type(a) # <class 'bytes'>

# Change Binary data to Data of Python
b = unpack('hhh', a)
b # (1, 2, 3)
type(b) # <class 'tuple'>

# Calculate data size
calcsize('hhh') # 6

"""
-- Alignment control --

text,byte order,size and alignment 
@,According to System,According to System
=,According to System,Standard
<,little-endian,Standard
>,big-endian,Standard
!,network(big-endian),Standard
"""

calcsize('i') # 4
calcsize('h') # 2
calcsize('hi') # 8
calcsize('>hi') # 6
