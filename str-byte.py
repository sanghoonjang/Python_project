
# string and byte
s = 'abcde' # string - unicode
b = b'abcde' # byte - 0~255


# Decode() - Byte to String
s2 = b.decode() # unicode
s2 # 'abcde'


# Encode() - String to Byte
b2 = a.encode()
b2 # b'abcde'


# bytearray() - Be able to change byte
ba = bytearray(b)
ba # bytearray(b'abcde')

ba[2] = ord('C') # ord() is to change text('C') to text number(67)
ba[2] = 67 # this is same
ba # bytearray(b'abCde')

b3 = bytes(ba)
b3  # b'abcde'

s3 = ba.decode()
s3 # 'abcde'
