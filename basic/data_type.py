# Variable
pi = 3.141592


# Text
spam = "spam"
spam2 = "sspam"

spam + spam2 # spamsspam


# List
temp = [25.5, 36.5, 10, 43, 27.1]

temp[0] # 25.5

temp[0] = 40
temp = [40, 36.5, 10, 43, 27.1]

del temp[0]
temp = [36.5, 10, 43, 27.1]

temp2 = temp[1:3]
temp2 # [10, 43]

temp[:2] # [36.5, 10]
temp[1:] # [10, 43, 27.1]

city_temps = [
  [14.0, 14.8, 15.1, 15.4, 15.2, 15.4, 17.0, 16.9]
  [10.0, 10.4, 11.5, 11.2, 10.9, 10.6, 11.8, 13.2]
  [16.0, 15.5, 16.4, 17.1, 14.2, 10.5, 12.6, 15.1]
]
city_temps[1] # [14.8, 14.8, 15.1, 15.4, 15.2, 15.4, 17.0, 16.9]
city_temps[1][1] # 14.8

team = [150, 160, 170, 180]
sum(team) # 660
min(team) # 150
max(team) # 180


# Dictionary
dic = {1:"apple",
       2:"banana",
       3:"orange",
       4:"kiwi"}

dic[1] # apple

dic[1] = "mango"
dic # {1:"mango", 2:"banana", 3:"orange", 4:"kiwi"}

dic[5] = "apple"
dic # {1:"mango", 2:"banana", 3:"orange", 4:"kiwi", 5:"apple"}

del dic[5]
dic # {1:"mango", 2:"banana", 3:"orange", 4:"kiwi"}


# Set
li = [1,1,1,2,3,4,5]
seet = set(li)
seet # {1,2,3,4,5}


# Tuple
month_name = ("January", "February", "March", "April", "May", "June", "July")
month_name[1] # February

month_name[0] = "hello" # Error
