
# string and byte
a = 'abcde' # string - unicode
b = b'abcde' # byte - 0~255


# Decode() - Byte to String
b2 = b.decode() # unicode
b2 # 'abcde'


# Encode() - String to Byte
a2 = a.encode()
a2 # b'abcde'


# bytearray() - Be able to change byte
bb = bytearray(b)
bb # bytearray(b'abcde')

bb[2] = ord('C') # ord() is to change text('C') to text number(67)
bb[2] = 67 # this is same
bb # bytearray(b'abCde')

bytes(bb) # b'abcde'

bb.decode() # 'abcde'
