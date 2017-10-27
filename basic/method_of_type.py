#문자열
str = "a b c d e"

str2 = str.replace("a", "f")
str2 # "f b c d e"

li = str2.split()
li # ["f", "b", "c", "d", "e"]

str3 = "/".join(li)
str3 # "f/b/c/d/e"

str.find("b") # 2
str.find("z") # -1

str.index("b") # 2
str.index("z") # ValueError

str.endswith("e") # True
str.endswith("a") # False
str.startswith("e") # False
str.startswith("a") # True

str.strip("a") # " b c d e"
str.strip("e") # "a b c d "
str.strip("b") # "a b c d e"

str_upper = str.upper() # "A B C D E"
str_lower = str_upper.lower() # "a b c d e"

"{} love you".format("i") # "i love you"

#리스트

#딕셔너리

#set

#tuple
