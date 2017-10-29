# text type
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
str4 = "   string   "
str4.strip() # "string"

str_upper = str.upper() # "A B C D E"
str_lower = str_upper.lower() # "a b c d e"

"{} love you".format("i") # "i love you"


# list type
team = [178, 154, 160, 180, 142]

team.sort()
team # [142, 154, 160, 178, 180]

li = [1,2,3,4,5]
li.reverse() # [5,4,3,2,1]
li.remove(3) # [5,4,2,1]
li.append(1) # [5,4,2,1,1]
li.extend([2,3,4]) # [5,4,2,1,1,2,3,4]
li.pop() # 4
li # [5,4,2,1,1,2,3]
li.index(5) # 0


# dictionary type
dic = {1:"apple",
       2:"banana",
       3:"orange",
       4:"kiwi"}

dic.update({1:"abokado", 5:"kaki"})
dic # {1: 'abokado', 2: 'banana', 3: 'orange', 4: 'kiwi', 5: 'kaki'}

dic.keys() # dict_keys([1, 2, 3, 4, 5])

dic.get(1) # "abokado"
dic.get(10,"empty") # empty
dic # {1: 'abokado', 2: 'banana', 3: 'orange', 4: 'kiwi', 5: 'kaki'}

dic.setdefault(1) # "abokado"
dic.setdefault(10, "empty")
dic # {1: 'abokado', 2: 'banana', 3: 'orange', 4: 'kiwi', 5: 'kaki', 10: 'empty'}

dic.items() # dict_items([(1, 'abokado'), (2, 'banana'), (3, 'orange'), (4, 'kiwi'), (5, 'kaki'), (10, 'empty')])

dic.values() # dict_values(['abokado', 'banana', 'orange', 'kiwi', 'kaki', 'empty'])


# set type
seet = {1,2,3,4,5}

seet.add(5)
seet # {1,2,3,4,5}

seet.remove(5)
seet # {1,2,3,4}
