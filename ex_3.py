# 1
print("------------------------ 1 + 2 ------------------------")
try:
    a = 1 / 0
except ZeroDivisionError:
    print("Zero Division Error!")
finally:
    print("Next Exercise")

# 3
print("------------------------ 3 ----------------------------")
# this code is legal
try:
    x = 1
finally:
    print("finally")


# 4
print("------------------------ 4 ----------------------------")
# Exception Types
# any exception


# 5
print("------------------------ 5 ----------------------------")
# when error occurs, there are many reasons for that,
# and when we use general exception, we can't handle each type of error.
# so, the best solution is to use exception type.

# 6
print("------------------------ 6  ----------------------------")
# except IOError
# Errors for file handling

# #except ZeroDivisionError
# Errors for division by Zero


# 7 - 8
print("------------------------ 7 - 8  ----------------------------")
myFile = open("C:/Yossi/DevOps/0520/3/words.txt", "w")
myFile.write("Yossi B")
myFile.close()


# 9
print("------------------------ 9  ----------------------------")
myFile = open("C:/Yossi/DevOps/0520/3/words.txt", "r")
content = myFile.read()
print(content)
myFile.close()


# 10
print("------------------------ 10  ----------------------------")
myFile = open("C:/Yossi/DevOps/0520/3/words.txt", "a", encoding='utf-8')
myFile.write("\n")
myFile.write("תרגיל מעולה לטיפול בקבצים!")
myFile.close()


# Challenge
print("------------------------ 11  ----------------------------")
from PIL import Image, ImageDraw, ImageFont
Img = Image.new("RGB", (400, 400), color = 'yellow')
Img.save('C:/Users/Yossi/PycharmProjects/prj2/media/pill_yellow.png')
# set font
fnt = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 25)
d = ImageDraw.Draw(Img)
d.text((50, 50), "My First Image", font = fnt, fill = (155, 155, 0))
Img.save('C:/Users/Yossi/PycharmProjects/prj2/media/pill_yellow-2.png')

