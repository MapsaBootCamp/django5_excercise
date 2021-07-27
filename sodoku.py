import numpy as np
import time

Puzzel = [
          [3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]
          ]

'''
حالا میخواییم لیست بالا رو به ماتریس 9*9 تبدیل کنیم 
 که شکل جدول به خودش بگیره

'''
start = time.time()
print(np.matrix(Puzzel))

'''
حالا باید چک کیم که عدد ورودی در هر سطر و ستون و حتی 
در  هر جدول 3*3 که این ماتریس از  9 تا جدول تشکیل شده 
خاص (بدون تکرار )باشه
در واقع سه تا شرط باید همزمان چک بشه

'''

def check(row , column , number):
    global Puzzel
    for i in range(9):
        if Puzzel[row][i] == number:
            return False
    for i in range(9):
        if Puzzel[i][column] == number:
            return False
    startcolumn = column - column % 3  # برای اینکه اندیس  هر خانه رو بدست بیاریم 
    startrow = row - row % 3  # برای اینکه اندیس  هر خانه رو بدست بیاریم  


    
    '''
سظر و ستون ها رو چک کردیم که تکراری نداشته باشیم 
حالا باید جدول های 3*3 رو چک کنیم
برای اینکار اولین خونه از هر جدول رو نیاز داریم 
چون سه تا سظر و سه تا ستون داره هر جدول
حاصل باقی مانده هر سطر به سه رو از خودش کم میکنیم

    '''


    for i in range (3):   # چون مربع ها  3*3 هستند پس اندیس از 0 تا 2 میشه یعنی رنج 3
        for j in range(3):
            if Puzzel[startrow + i][startcolumn +j] == number :
                return False
    return True

def solve():
    global Puzzel
    for row in range(9):
        for column in range(9):
            if Puzzel[row][column] == 0:
                for number in range(1,10):
                    if check(row , column , number):
                        Puzzel[row][column] = number
                        solve()
                        Puzzel[row][column] = 0
                return
    print(np.matrix(Puzzel))


print("------------------------------")
solve()
end = time.time()
print(f"Execution time is: {end - start}")