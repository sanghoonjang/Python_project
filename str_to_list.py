
# Change string of numbers to list

str = "1,2,3,4,5,6,7"

li_str = str.split(",")
li_str # ['1', '2', '3', '4', '5', '6', '7']

li_num = list(map(lambda n: int(n), li_str))
li_num # [1, 2, 3, 4, 5, 6, 7]


# --- Note --- 

num_front = li_num.pop(0)
num_front # 1

num_lear = li_num.pop()
num_lear # 7

li_num # [2, 3, 4, 5, 6]
