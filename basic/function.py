# Set a function

# lambda ( Instant function )

# Conprehension 
str_speeds = "38 42 20 40 39"
speeds = [int(s) for s in str_speeds.split()]
speeds # [38, 42, 20, 40, 39]

str_speeds2 = "38 42 20 40 a1 39"
speeds2 = [int(s) for s in str_speeds2.split() if s.isdigit()]
speeds2 # [38, 42, 20, 40, 39]

dic = {1:"apple",
       2:"banana",
       3:"orange",
       4:"kiwi"}
fru = {val:key for key, val in dic.items()}
fru # {'apple': 1, 'banana': 2, 'orange': 3, 'kiwi': 4}

li = ["DUCK", "CAT", "dog"]
ani = {x.lower() for x in li}
ani # {'cat', 'dog', 'duck'}
