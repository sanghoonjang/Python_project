
# test.txt
# aaaaaaaa
# bbbbbbbb
# cccccccc
# dddddddd


# Text file
f = open("test.txt", "r", encoding="utf-8")
s = f.read()
print(s)
f.close()

f.readline()
f.readlines()

f = open("test2.txt", "w", encoding="utf-8")
f.write("ffffffffffff")
f.close()


# Binary file
imgfile = open("test.png", "rb")
imgsrc = imgfile.read()
if imgsrc[1:4] == b"PNG":
  print("image/png")

