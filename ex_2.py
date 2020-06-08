import re

# A
print("======================= A ============================")
x = 10
y = 5
if x > y:
    print("BIG")
elif x < y:
    print("small")


# B
print("======================= B ============================")
for num in range(5):
    print(num, end='---')


# C
print("======================= C ============================")
x = 3
if x == 1:
    print("summer")
elif x == 2:
    print("winter")
elif x == 3:
    print("fall")
elif x == 4:
    print("sprint")
else:
    print("between seasons")


# D
print("======================= D ============================")
# 1. 10 times
# 2. Output : 10
count = 1
while count < 11:
    print(count)
    count = count + 1


# E
print("======================= E ============================")
age = 44
last_name = "b"
currency = 3.70
isflew = True
apt_num = 38

print(age)
print(last_name)
print(currency)
print(isflew)
print(apt_num)
print(currency + age)


# F
print("======================= F ============================")


def valid_phone(p):
    rule = re.compile(r'^[-+]?[0-9]+$')
    if not rule.search(p):
        return False
    else:
        return True

# phone = str(input("Enter Phone:"))


phone = "+972503333444"
if valid_phone(phone):
    print("phone number " + phone)
else:
    print("Error phone input")


# G
print("======================= G ============================")

def printHello():
    print("hello")

def calculate():
    print(5 + 3.2)

printHello()
calculate()

# H
print("======================= H ============================")


def printname(n = ''):
    print(n)


def div_by_two(num = 0):
    print(num / 2)


printname("yossi")
div_by_two(9)


# I
print("======================= I ============================")


def calc_sum(n1, n2):
    return n1 + n2


def merge_string(s1, s2):
    return s1 + " " + s2


print(calc_sum(33, 55))
print(merge_string("yossi", "basson"))

# K
print("======================= k ============================")
for x in range(1, 6, 1):
    s = ""
    for y in range(x):
        s = s + "#"
    print(s)

# l
print("======================= l ============================")

for x in range(1, 8):
    s = ""
    for y in range(1, 8):
        if (y >= x and y < x+1) or (y == 8-x):
            s = s + "*"
        else:
            s = s + " "
    print(s)


# M
print("======================= M ============================")


def get_nums():
    count = 0
    num_input = 2
    arrNums = []
    while count < num_input:
        num = str(input("Enter Number: "))
        arrNums.append(num)
        count += 1
    return arrNums


def comp_sum(n):
    sum = 0
    num = int(n)
    lnums = list(str(num))
    for ln in lnums:
        sum += int(ln)
    return sum


arrNums = get_nums()
for n in arrNums:
     # print(n, end=' ')
     print("Sum of " + n + " Digits: " + str(comp_sum(n)))


