
# #region bai1
# # #1
# # print("Twinkle, twinkle, little star,\n \tHow I wonder what you are!\n \t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
# # ------------------------------

# # #2
# # import sys
# # print(sys.version)
# # ------------------------------

# # #3
# # import datetime
# # timenow = datetime.datetime.now()
# # print(timenow)
# # ------------------------------

# # #4
# # from math import pi
# # r = float(input("input radius:" ))
# # print("area: "+ str(pi * r**2))
# # ------------------------------

# # #5
# # first_name = input("input first name: ")
# # last_name = input("input last name: ")
# # print(last_name, first_name)
# # ------------------------------

# # #6
# # nums = input("input a number list: ")
# # list = nums.split(",")
# # tuple = tuple(list)
# # print(list)
# # print(tuple)
# # ------------------------------

# # #7
# # filename = input("input file name: ")
# # file_extent = filename.split(".")
# # print("file type is:", file_extent[-1])
# # ------------------------------

# # #8
# # color_list = ["Red","Green","White" ,"Black"]
# # print(color_list[0],color_list[-1],)

# # 9
# # exam_st_date = (11, 12, 2014)
# # exam_st_date2 = [11, 12, 2014]
# # print("%i / %i / %i"%exam_st_date)
# # print("{}/{}/{}".format(*exam_st_date))
# # ------------------------------

# # 10
# # def calculate_integer_series(start, base):
# #     root = start
# #     result = 0
# #     for i in range(base):
# #         print(start)
# #         result += start
# #         start = start * 10 + root
# #     print(result)

# # calculate_integer_series(5, 3)
# # ------------------------------


# # #11
# # print(abs.__doc__)
# # ------------------------------

# # # 12
# # import calendar

# # y = int(input("Input the year : "))
# # m = int(input("Input the month : "))
# # print(calendar.month(y, m))
# # ------------------------------

# # 13
# # print("""
# # a string that you "don't" have to escape
# # This
# # is a  ....... multi-line
# # heredoc string --------> example
# # """)
# # ------------------------------

# # # 14
# # from datetime import date

# # f_date = date(2023, 8, 1)
# # l_date = date(2023, 8, 10)
# # delta = l_date - f_date
# # print(delta.days)
# # ------------------------------


# # 15
# # import math

# # def get_volume(r):
# #     return 4 / 3 * math.pi * r**3

# # print(get_volume(6))

# # r = int(input("Nhap ban kinh: "))
# # print("the tich hinh cau ban kinh r: {} la {}".format(r, 4 / 3 * math.pi * r**3))
# # -------------------


# # # 16
# # def difference(n):
# #     if n <= 17:
# #         return 17 - n
# #     else:
# #         return (n - 17) * 2


# # print(difference(22))
# # print(difference(14))
# # ------------------------------


# # # 17
# # def kiem_tra(n):
# #     return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)

# # print(kiem_tra(600))
# # ------------------------------


# # # 18
# # def sum(a, b, c):
# #     if a == b == c:
# #         return a**3
# #     return a + b + c


# # print(sum(3, 3, 3))
# # ------------------------------

# # 19
# # def new_string(text):
# #   if len(text) >= 2 and text [:2] == "Is":
# #     return text
# #   return "Is" + text
# # print(new_string("Array"))
# # print(new_string("IsEmpty"))
# # ------------------------------


# # # 20
# # def copy(string, time):
# #     result = ""
# #     for x in range(time):
# #         result = result + string
# #     return result

# # print(copy("ab", 3))
# # ------------------------------


# # # 21
# # def check_number(n):
# #     if n % 2 == 0:
# #         return "{} is even".format(n)
# #     return "{} is odd".format(n)

# # print(check_number(15))
# # print(check_number(8))
# # ------------------------------


# # 22
# # def count_4(list):
# #     count = 0
# #     for num in list:
# #         if num == 4:
# #             count += 1
# #     return count

# # print(count_4([1, 2, 3, 4, 4]))
# # ------------------------------


# # 23
# # def copy_2_first_char(string, time):
# #     result = ""
# #     if len(string) < 2:
# #         result = string
# #     else:
# #         for x in range(time):
# #             result = result + string[0:2]
# #     return result


# # print(copy_2_first_char("abcde", 3))
# # print(copy_2_first_char("fg", 2))
# # ------------------------------


# # 24
# # vowels = ["o","e","a","o","i"]
# # def is_vowel(char):
# #     if char in vowels:
# #         return True
# #     return False

# # print(is_vowel("w"))
# # ------------------------------

# # 25
# # def contain(data, n):
# #     for value in data:
# #         if n in data:
# #             return True
# #         return False
# # print(contain([1,2,3,4], 5))
# # ------------------------------
# #endregion

# #region bai2



# # ------------------------------



# #1 Tinh
# #a) a + b
# def Sum(a,b):
#     return a + b
# #b) a / b
# def Dev(a,b):
#     return a / b
# #c) a^b
# def Exponential(a,b):
#     return a**b
# #2 Tính diện tích hình chữ nhật khi biết bán kính
# def Rectangular_area(a,b):
#     return a*b
# #3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range (2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def PrintPrimeNumber(n):
#     prime_numbers = []
#     for i in range(2,n+1):
#         if(isPrime(i)):
#             prime_numbers.append(i)
#     return prime_numbers
# #4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
# def Is_Fibonacci(n):
#     a, b = 0, 1
#     while b < n:
#         a, b = b, a + b
#     if b == n or n == 0:
#         return "Day la Fibonacci"
#     return "Khong phai Fibonacci"
# #Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
# #Đệ quy
# def fibonacci(n):
#     if n <= 0:
#         return "Vui lòng nhập một số nguyên dương > 0"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# #Không đệ quy   
# def fibonacci2(n):
#     if n <= 0:
#         return "Vui lòng nhập một số nguyên dương > 0"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         a,b = 0,1
#         i = 0
#         while i < n - 2:    
#             a, b = b, a + b
#             i += 1
#         return b
# #6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)
# def Sum_fibonacci(n):
#     sum = 0
#     for i in range(1,+n+1):
#         sum += fibonacci(i)
#     return sum
# #7. Tính tổng căn bậc 2 của n số nguyên đầu tiên
# def Sum_sqrt(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += math.sqrt(i)
#     return sum
# #8. Giải phương trình bậc 2: ax2 + bx + c=0
# def QuadraticEquation(a,b,c):
#     delta = (b**2) - 4*a*c
#     if delta < 0:
#         return "Phương trình vô nghiệm."
#     elif delta == 0:
#         x = -b / (2*a)
#         return f"Phương trình có nghiệm kép x = {x}"
#     else:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         return f"Phương trình có hai nghiệm x1 = {x1} và x2 = {x2}"
# #9. Tính n!
# def Factorial(n):
#     factorial = 1
#     for i in range(1, n+1):
#         factorial *= i
#     return factorial
# #10.In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
# def PrintTriangle(n):
#     for i in range(n):
#         for j in range(i+1):
#             if j == 0 or j == i or i == n-1:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
# #11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.
# from datetime import datetime
# def ConvertTime(sec):
#     hour = sec // 3600
#     minute = (sec % 3600) // 60
#     sec = (sec % 3600) % 60
#     return f"{hour}:{minute}:{sec}"



# #songuyento
def ktra_nguyento(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

import math
my_array = [i for i in range(1, 201)]

odd_numbers = [i for i in my_array if i % 2 != 0]

odd_numbers2 = [i for i in my_array if i & 1 == 1]

even_numbers = [i for i in my_array if i % 2 == 0]

# fibonaci
def is_perfect_square(n):
    sqrt_n = int(n**0.5)
    return sqrt_n * sqrt_n == n

def is_fibonacci(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)
#12 a Xuat so le ko chia het cho 5
khongchiahetcho5_1 = [i for i in range(1, 201) if i % 2 != 0 and i % 5 != 0]
khongchiahetcho5 = [i for i in odd_numbers if i % 5 != 0]
#12 b Xuat fibonacci
def find_fibonacci(array):
    return [i for i in array if is_fibonacci(i)]

#12 c So nguyen to lon nhat
songuyento = [i for i in my_array if ktra_nguyento(i)]
songuyento_lonnhat = songuyento[-1]

#12 d fibonacci be nhat
fibonacci = find_fibonacci(my_array)
fibonacci_benhat = fibonacci[0]

# 12 e Trung binh so le
def tb_sole(array):
    sum = 0
    for i in array:
        sum += i
    return sum

tb_sole2 = sum (x for x in  [1, 2, 3, 4])
print(tb_sole2)



#12 f so le ko chia het cho 3
def sole_khongchiahet3(array):
    kochiahet3 = []
    for i in array:
        if i % 3 != 0:
            kochiahet3.append(i)
    return kochiahet3
sole_khongchiahet3(odd_numbers)

#12 g doi cho 2 phan tu
def doi_cho(array, stt1, stt2):
    array[stt1], array[stt2] = array[stt2], array[stt1]
    return array

#12 h dao nguoc danh sach
array = [1, 2, 3, 4, 4, 5]
array.reverse()
array[::-1]

#12 i  xuat so lon thu 2
def second_largest(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[1] if len(sorted_numbers) >= 2 else None

def second_largest2(numbers):
    if len(numbers) < 2:
        return "Không đủ số để tìm số lớn thứ nhì"
    
    sorted_numbers = sorted(numbers, reverse=True)
    second_largest = sorted_numbers[1]
    return second_largest

def second_largest3(numbers):
    if len(numbers) < 2:
        return "Không đủ số để tìm số lớn thứ nhì"
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest
print(second_largest(array))

#12 j tinh tong cac chu so trong danh sach
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def total_sum_of_digits1(numbers):
    total = 0
    for num in numbers:
        total += sum_of_digits(num)
    return total

def total_sum_of_digits2(numbers):
    total = 0
    for num in numbers:
        while num > 0:
            total += num % 10
            num //= 10
    return total

#12 k 
def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

#endregion

#region
# #1
# string = "thanh"
# if string == "malayalam":
#     print("yes")
# else:
#     print("no")
# #2

# #3
# string = "hello toi di code dao"
# rs = string.split()[::-1]
# #4
# string = "thanh123thanh123"
# check = "123"
# rs = string.replace(check, "")
# #5
# string = "given string"
# sub_string = "given"

# if sub_string in string:
#     print("yes")
# else:
#     print("no")
# #6
# string = "doan van mau"
# res = {key: string.count(key) for key in string.split()}
 
# #print("The words frequency : " + str(res))
# #7
# string = "doan_van_mau"
# rs = string.replace("_", " ").title().replace(" ", "")
# #8
# string = "t h a n h"
# print(len(string))
# #9
# string = "i am you ammm"
# s = string.split()

# for i in s:
#     if len(i) % 2 == 0:
#         print(i + " ")
# #10

#11
#12
#13
#14
#15
#16
#17
#18
#19
#20
#21
#22
#23
#24
#25
#26
#27
#28
#29
#30
#endregion


# import string
# import random
# import time
# from collections import Counter
# #10
# vowels = ['a', 'e', 'i', 'o', 'u']
# def Check(string):
#     string = string.lower()
#     s = set({})
#     for char in string:
#         if char in vowels:
#             s.add(char)
#         else:
#             pass
#     if len(s) == len(vowels):
#         print("accept")
#     else:
#         print("no accept")
# #11 
# def count_match(str1, str2):
#     return(len((set(str1)).intersection(set(str2))))
# #12
# def removeDuplicate(string):
#     s = set(string)
#     return "".join(s)
# #13
# def least_fre(string):
#     res = Counter(string)
#     return min(res, key = res.get)
# #14
# def max_fre(string):
#     res = Counter(string)
#     return max(res, key = res.get)
# #15 
# spec_char =  "[@_!#$%^&*()<>?}{~:]"
# def check_spec_char(string):
#     for  c in string:
#         if c in spec_char:
#             return True
#     return False
# #16

# #17

