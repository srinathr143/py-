# string reversal without typecasting

# s='srinath'
# rev=''
# i=0
# while i<len(s):
#     rev=s[i]+rev
#     i+=1
# print(rev)

# bus ticket booking


# dic={'vadapalani':1,'arumbakam':2,'koyambedu':3,'anna nagar':4,'guindy':5,'tambaram':6}
# start=input("enter the source:").lower()
# end=input("enter the destination:").lower()
# gender=input('enter your gender:').lower()
# category=int(input('enter 1.adult \n 2.child\n'))
# if gender=='male':
#     if category==1:
#         t_price=(dic[end]-dic[start])*5
#         print('-'*30)
#         print(f'welcome to MTC')
#         print(f'starting station:{start}')
#         print(f'ending station:{end}')
#         print(f'fare:{t_price}')
#         print(f'Happy journey....')
#         print('-' * 30)
#
#     else:
#         t_price = (dic[end] - dic[start]) * 2
#         print('-' * 30)
#         print(f'welcome to MTC')
#         print(f'starting station:{start}')
#         print(f'ending station:{end}')
#         print(f'fare:{t_price}')
#         print(f'Happy journey....')
#         print('-' * 30)
#
# elif gender=='female':
#     print('-' * 30)
#     print(f'welcome to MTC')
#     print(f'starting station:{start}')
#     print(f'ending station:{end}')
#     print(f'fare:{0}')
#     print(f'Happy journey....')
#     print('-' * 30)
# lst = ['apple', 'banana', 'mango', 'orange', 'tamarind']
# lst1 = []
# i = 0
# while i < len(lst):
#     if len(lst[i]) % 2 == 0:
#         lst1.append(lst[i])
#     else:
#         a=lst[i][:len(lst[i])//2]
#         lst1.append(a)
#     i += 1
# print(lst1)

# strong number

# n=int(input('enter the number :'))
# no=n
# sum=0
# while n>0:
#     temp =n%10
#     fact=1
#     while temp>0:
#         fact *= temp
#         temp -= 1
#     sum+=fact
#     n//=10
# if no==sum:
#     print('strong number')
# else:
#     print('not a strong number')

# fibonacci series

# n=int(input("enter the value:"))
# a=0
# b=1
# print(a,b,end=' ')
# i=1
# while i<n-1:
#     c=a+b
#     print(c,end=' ')
#     a=b
#     b=c
#     i+=1

# fibonacci series for the n number

# n=int(input("enter the value:"))
# a=0
# b=1
# print(a,b,end=' ')
# i=1
# while i<n-1:
#     c=a+b
#     if c<=n:
#         print(c,end=' ')
#     else:
#         break
#     a = b
#     b = c

# armstrong number

# n = int(input('enter the value:'))
# count = len(str(n))
# sum=0
# no = n
# while n > 0:
#     temp = n % 10
#     sum +=temp ** count
#     n //= 10
# if no == sum:
#     print("armstrong number")
# else:
#     print('not a armstrong number')

# Armstrong number without any typecasting

# n = int(input('enter the input:'))
# n1 = n
# n2 = n
# count = 0
# sum1 = 0
# while n > 0:
#     count += 1
#     n //= 10
# while n1 > 0:
#     temp = n1 % 10
#     sum1 += temp ** count
#     n1 //= 10
# if n2 == sum1:
#     print('Armstrong number')
# else:
#     print('not a Armstrong number')

# xylem or phloem

# n=int(input('enter the value:'))
# s=str(n)
# e_s=int(s[0])+int(s[-1])
# m_s=0
# i=1
# while i<len(s)-1:
#     m_s+=int(s[i])
#     i+=1
# if e_s == m_s :
#     print('xylem')
# else:
#     print('phloem')

# xylem or phloem without using typecast operator

# n=int(input('enter the values:'))
# n1=n
# o_sum=0
# i_sum=0
# i=0
# while n>0:
#     r=n%10
#     if n==n1 or n<10:
#         o_sum+=r
#     else:
#         i_sum+=r
#     n//=10
# if o_sum==i_sum:
#     print('xylem')
# else:
#     print('phloem')

# happy number or not

# n = int(input('enter a number:'))
# i = 0
# while n > 9:
#     sum = 0
#     while n > 0:
#         r = n % 10
#         sum += r ** 2
#         n //= 10
#     n = sum
# if n == 1:
#     print('happy number')
# else:
#     print('not a happy number')

# wap to create a list from an old list if the elements
# present in the list having even length of characters
# add as it is else add first half in a reverse order

# l = ['apple', 'umbrella', 'facebook', 'instagram', 'twitter']
# l1 = []
# i = 0
# while i < len(l):
#     if len(l[i]) % 2 == 0:
#         l1.append(l[i])
#     else:
#         a = l[i][:len(l[i]) // 2][::-1]
#         l1.append(a)
#     i += 1
# print(l1)

# wap to create a list with tuple of elements is having even length else elements and length

# l = ['neem', 'dinga', 'tamarind', 'sunflower', 'potato','orange']
# res=[]
# i=0
# while i<len(l):
#     if len(l[i])%2==0:
#         res.append((l[i],i))
#     else:
#         res.append((l[i],len(l[i])))
#     i+=1
# print(res)

# wap to create a list from a string if the element present
# in a string are vowels add ASCII value else add elements in uppercase

# s='apple'
# res=[]
# i=0
# while i<len(s):
#     if s[i] in 'aeiouAEOIU':
#         res.append(ord(s[i]))
#     else:
#         res.append(s[i].upper())
#     i+=1
# print(res)
#
# wap to create key from list with key as first half and value as second half
#
# l = ['apple', 'umbrella', 'facebook', 'instagram', 'twitter']
# dic={}
# i=0
# while i<len(l):
#     f=l[i][:len(l[i])//2]
#     s=l[i][len(l[i])//2:]
#     dic[f]=s
#     i+=1
# print(dic)
#
# wap to create dictionary from list with element and length
# pair if element is having odd length else element first half pair
#
# l = ['apple', 'umbrella', 'facebook', 'instagram', 'twitter']
# dic = {}
# i = 0
# while i < len(l):
#     if len(l[i]) % 2 == 1:
#         dic[l[i]] = len(l[i])
#     else:
#         dic[l[i]] = l[i][:len(l[i]) // 2]
#     i += 1
# print(dic)
#
# wap to create a list from tuple by making square of number if the number is even else cube of number
#
# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# l = []
# i = 0
# while i < len(a):
#     if a[i] % 2 == 0:
#         l.append(a[i] ** 2)
#     else:
#         l.append(a[i] ** 3)
#     i += 1
# print(l)
#
# wap to traverse through string and create a dictionary with key as element and value as opposite case of element
#
# s = 'AiLE'
# d = {}
# i = 0
# while i < len(s):
#     if s[i].lower():
#         d[s[i]] = chr(ord(s[i]) + 32)
#     else:
#         d[s[i]] = chr(ord(s[i]) - 32)
#     i += 1
# print(d)
#
# wap to create a dictionary from a list with key as elements and value as index of the element
#
# l = ['dinga', 'dingi', 'manga', 'sanga', 'sangi']
# dic = {}
# for i in range(len(l)):
#     dic[l[i]] = i
# print(dic)
#
# wap to create a dic from name and salary list with a hike of 15%
#
# n = ['dinga', 'dingi', 'manga', 'mangi']
# s = [1000, 2000, 500, 2300]
# dic = {}
# for i in range(len(n)):
#     dic[n[i]] = s[i] + s[i] * 15 // 100
# print(dic)

# wap to print values and its datatype

# l = [1, 1, 2, True, 10 + 2j, 'hello', [1, 2, 3], (4, 5, 6), {1, 2, 3}, {'a': 1, 'b': 2}]
# dic={}
# for i in l:
#     print(f'{i} is a type of {str(type(i))[7:-1]}')

# wap to create a list if the elements are having length more than 6
#
# k = ['apple', 'banana', 'dinga', 'qspiders', 'pyspiders']
# res = []
# for i in k:
#     if len(i) > 6:
#         res.append(i)
# print(res)

# wap to check whether the given number is prime number or not

# n = int(input('enter the value:'))
# if n <= 1:
#     print('you entered 1')
# for i in range(2, n):
#     if n % 2 == 0:
#         print("not a prime number")
#         break
# else:
#     print('prime number')

#  prime number between 1 and n number

# n=int(input('enter a number:'))
# for i in range(2,n+1):
#     c=0
#     for j in range(2,i):
#         if i%j==0:
#             c+=1
#             break
#     if c==0:
#         print(i,end=' ')

# n = int(input('enter value of n number:'))
# for i in range(1, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')

# wap to create a dictionary from a set with index and length pair

# s={111,2222,33333,545454,64,1}
# s1=list(s)
# dic={}
# for i in range(len(s1)):
#     dic[s1[i]]=i
# print(dic)

# wap to create a dict by separating flowers,fruits and plants

# lst=['rose flower','neem plant','jasmine flower','apple fruit','tamarind plant','money plant','orange fruit']
# dic={}
# for i in lst:
#     value,key=i.split()
#     if key not in dic:
#         dic[key]=[value]
#     else:
#         dic[key].append(value)
# print(dic)

# wap to traverse through elements in the dictionary if the value is even add 15 else if it is odd add 10

# dic = {'apple': 1000, 'mango': 1235, 'orange': 230, 'grapes': 1111}
# res={}
# for i in dic:
#     if dic[i]%2==0:
#         res[i]=dic[i]+15
#     else:
#         res[i]=dic[i]+10
# print(res)
#
# dic = {'apple': 1000, 'mango': 1235, 'orange': 230, 'grapes': 1111}
# res={}
# for i,j in dic.items():
#     if j%2==0:
#         res[i]=j+15
#     else:
#         res[i]=j+10
# print(res)

# dic = {'apple': 1000, 'mango': 1235, 'orange': 230, 'grapes': 1111}
# for i in dic:
#     if dic[i] % 2 == 0:
#         dic[i] += 15
#     else:
#         dic[i] += 10
# print(dic)

# s = "A man, a plan, a canal: Panama"
# r=s.replace(' ','')
# s1=''
# for i in r:
#     if i.isalnum():
#         s1+=i
# if s1.lower()==s1.lower()[::-1]:
#     print('palindrome')
# else:
#     print('not a palindrome')
#
# print(s1)


# class Solution:
#     def isHappy( n: int) -> bool:
#         for i in range(9):
#             sum=0
#             for i in range(10):
#                 r=n%10
#                 sum+=r**2
#                 n//=10
#             n=sum
#         if n==1 or n==7:
#             return True
#         else:
#             return False
#     print(isHappy(19))

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         s=set()
#         for i in nums:
#             if i in s:
#                 return True
#             s.add(i)
#         return False

# s,t = "anagram", "nagaram"
# s1=sorted(s)
# t1=sorted(t)
# print(s,t)
# if s1==t1:
#     print(True)
# else:
#     print(False)
# if s==t:
#     print(True)
# else:
#     print(False)

# n = 5
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==j or i==n-1 or (i==2 and j==1) or (i==3 and j==1) or (i==3 and j==2):
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# o/p -->
# *
# * *
# * * *
# * * * *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(n):
#         if j==n-1 or i==n-1 or i+j==n-1 or (i==2 and j==3) or (i==3 and j==3) or (i==3 and j==2):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# o/p -->
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(n):
#         if j==n//2 or i==n-1 or (i==3 and j!=0 and j!=n-1) :
#             print('',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     print('' * (5 - i), end='')
#     print('* '*i,end='')
#     # print(''*(5-i),end='')
#     print()
# for i in range(4,0,-1):
#     print('' * (5 - i), end='')
#     print('* ' * i, end='')
#     print()

# o/p--->
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1,6):
#     print(' ' * (5-i), end='')
#     print('*'*i,end='')
#     # print(''*(5-i),end='')
#     print()
# for i in range(4,0,-1):
#     print(' ' * (5-i), end='')
#     print('*' *i, end='')
#     print()

# nums=[9,6,4,2,3,5,7,0,1]
# r=0
# n=len(nums)
# for i in nums:
#     r+=i
# e_sum=n*(n+1)//2
# a_sum=e_sum-r
# print(a_sum)

# n=[0,1,0,3,12]
# i=0
# l=len(n)
# while i<l:
#     if n[i]==0:
#         n.pop(i)
#         n.append(0)
#         l-=1
#     else:
#         i+=1
# print(n)

# n=-1
# l=[]
# for i in range(20):
#     l.append(3**i)
# if n in l:
#     print(True)
# else:
#     print(False)
# --------------------------------------------------------------------------
# 392 -is subsequence
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i=0
#         j=0
#         while i<len(s) and j<len(t):
#             if s[i]==t[j]:
#                 i+=1
#             j+=1
#         if i==len(s):
#             return True
#         else:
#             return False

# nums=[1,2,2,5,3,5]
# nums.sort()
# print(nums)
# l=[]
# for i in nums:
#     if i not  in l:
#         l.append(i)
# print(l)
# if len(l)>2:
#     print(l[-3])
# else:
#     print(l[-1])

# s = "Hello, my name is John"
# l=s.split()
# print(len(l))

# nums = [4,3,2,7,8,2,3,1]
# l=[]
# for i in range(1,len(nums)+1):
#     if i not in nums:
#         l.append(i)
# print(l)

# s = "abcabcabcabc"
# r=s+s
# print(r)
# d=r[1:-1]
# print(d)

# nums=[1,0,1,1,0,1]
# count=0
# max_count=0
# for i in range(len(nums)):
#     if nums[i]==1:
#         count+=1
#         max_count=max(max_count,count)
#     else:
#         count=0
# print(max_count)
#
# TWO SUM
#
# nums=[3,2,4]
# target=6
# f=len(nums)
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print([i,j])

# n=5
# n1=bin(n)
# p=str(n1)[2:]
# print(p)
# r=p.replace('1','2').replace('0','1').replace('2','0')
# print(str(r))
# i=int(r,2)
# print(i)

# n=10
# f1=0
# f2=1
# print(f1,f2,end=' ')
# for i in range(n):
#     f3=f1+f2
#     f1=f2
#     f2=f3
#     print(f3,end=' ')
# n=5
# if n==1 or n==2:
#     print(1)
# else:
#     lst=[0,1]
#     for i in range(n):
#         lst.append(lst[-1]+lst[-2])
#     print(lst[n])

# num = 28
# l=[]
# for i in range(1,num):
#     if num%i==0:
#         l.append(i)
# print(sum(l))

# n='USA'
# s=''
# for i in range(len(n)):
#     if n[i].isupper():
#         s+=n[i]
# print(s)
# if s==n:
#     print(True)
# else:
#     print(False)

# words = ["bella", "label", "roller"]
# l=[]
# for i  in range(len(words)):
#     if words[i][i] not in l:
#         l.append(words[i][i])
# print(l)

# x = 123
# temp=0
# while x>0:
#     a=x%10
#     temp*=10+a
#     x//=10
# print(temp)

# r=0
# i=0
# while i>0:
#     r=x%10
#     i-=1
# print(r)


# nums = [3,1,3,4,2]
# count={}
# for i in nums:
#     count[i]=count.get(i,0)+1
# print(count)
# for i,j in count.items():
#     if j>1:
#         print(i)

# s = "the sky is blue"
# s1=s.split()
# s1.reverse()
# print(s1)
# print(' '.join(s1))

# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
# s=set(nums)
# print(s)
# print(list(s)[len(s)-k])

# nums = [4,3,2,7,8,2,3,1]
# s=set()
# d=set()
# for i in nums:
#     if i in s:
#         d.add(i)
#     else:
#         s.add(i)
# print(list(d))

# digits = [1,2,3]
# s=''
# for i in digits:
#     s+=str(i)
#
# r=int(s)+1
# r1=str(r)
# res=[]
# for i in r1:
#     res.append(int(i))
# print(res)

# nums1 = [1,2]
# nums2 = [3,4]
# num=nums1+nums2
# r=sorted(num)
# m=len(r)//2
# if len(r)%2==0:
#     print((r[m-1]+r[m])/2)
# else:
#     print(r[m])

# def outer(func):
#     def inner(*args, **kwargs):
#         print('your output is :')
#         func(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def add(*args, **kwargs):
#     print(sum(args) + sum(kwargs.values()))
#
#
# add(1, 3, 4, 5, a=2, b=9)

# from time import sleep
#
#
# def outer(func):
#     def inner(*args, **kwargs):
#         print('wait 5 seconds your output is generating.......')
#         sleep(5)
#         func(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def add(*args, **kwargs):
#     print(sum(args) + sum(kwargs.values()))
#
#
# add(1, 3, 4, 5, a=2, b=9)

#
# from time import sleep, time
#
#
# def outer(func):
#     def inner(*args, **kwargs):
#         start = time()
#         print('Thanks for waiting here is your output:', end=' ')
#         func(*args, **kwargs)
#         stop = time()
#         print(f'Starting time:{int(start)} \nEnding time:{int(stop)} \nExecution time:{int(stop - start)}')
#
#     return inner
#
#
# @outer
# def add(*args, **kwargs):
#     sleep(2)
#     print(sum(args) + sum(kwargs.values()))
#
#
# add(1, 2, 34, 5, a=3, b=7)


# def outer(func):
#     def inner(a, b):
#         if b == 0:
#             a, b = b, a
#             func(a, b)
#         else:
#             func(a, b)
#
#     return inner
#
#
# @outer
# def div(a, b):
#     print(a // b)
#
#
# div(4, 0)

# class Solution:
#     def add(self, a, b):
#         print(a + b)
#
#
# # a = Solution()
# Solution.add(Solution,3,5)

# class Bank:
#     b_name = 'SBI'
#     ifsc_code = 'SBI0000123'
#     loc = 'vadapalani'
#
#     def __init__(self, c_name, ph_no, address):
#         self.c_name = c_name
#         self.ph_no = ph_no
#         self.address = address
#
#
# b1 = Bank('Srinath',9940628990,'Tiruninravur')
#
# b2 = Bank('Soundarya',9840223896,'veppempattu')
#
# b3 = Bank('Ramesh Babu',9940036262,'guindy')
#
#
# print(f'Bank Name:{b1.b_name} \nIfsc_code:{b1.ifsc_code}\nLocation:{b1.loc}\n')
# print('*'*23)
# print(f'\nCustomer Name:{b1.c_name}\nCustomer phone number:{b1.ph_no}\nAddress:{b1.address}')
# print('*'*23)
# print(f'\nCustomer Name:{b2.c_name}\nCustomer phone number:{b2.ph_no}\nAddress:{b2.address}')
# print('*'*23)
# print(f'\nCustomer Name:{b3.c_name}\nCustomer phone number:{b3.ph_no}\nAddress:{b3.address}')


# class Car:
#     def Car_type(self):
#         print('4 seater')


# class Bike:
#     def Bike_type(self):
#         print('Racing bike')
#
#
# class Vehicle(Car, Bike):
#     def vehicle_type(self):
#         print('High end')
#
#
# class BMW(Vehicle):
#     def electric(self):
#         print('i70 model')
#
#
# class Honda(Vehicle):
#     def Automatic(self):
#         print('Honda CB250T')
#
#
# v=Vehicle()
# b=BMW()
# h=Honda()
# v.Car_type()
# v.Bike_type()
# v.vehicle_type()

# class Solution:
#     def add(self,a,b):
#         print(a+b)
# a1=Solution()
# a=int(input('enter the value1:'))
# b=int(input('enter the value2:'))
# a1.add(a,b)
#
# t=('hello')
# print(t)


# def hu():
#     t = (1, 2, 3, 4, 5, 6, 7, 8)
#     try:
#         u=t[8]
#         print(u)
#     except IndexError  :
#         print('i catched the error')
#
#
# hu()

# class Solution:
#     def Fib(self, n):
#         ans = [0, 1]
#         for i in range(2, n + 1):
#             ans.append(ans[i - 1] + ans[i - 2])
#         return ans
#
#
# s = Solution()
# print(*s.Fib(10))


# def d(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return d(n - 1) + d(n - 2)
#
#
# print(d(10))

"""
# n = range(1, 100)
#
#
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#
#     return True
#
#
# primes = list(filter(prime, n))
# print(*primes)

"""
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')  # Start with infinity, so any price will be smaller

        # Step through each price in the list
        for i in prices:
            # If the current price is smaller than the minimum price, update min_price
            if i < min_price:
                min_price = i
            # Calculate the profit by selling at the current price and buying at min_price
            profit = i - min_price
            # If this profit is larger than the maximum profit so far, update max_profit
            if profit > max_profit:
                max_profit = profit

        # Return the maximum profit found
        return max_profit



with prices =[7, 1, 5, 3, 6, 4]

Initialization:

max_profit = 0: No profit has been made yet.
min_price = float('inf'): This starts as infinity so that any price will become the new minimum.

Day 1(Price=7):

min_price = 7: The price 7 is smaller than infinity, so we update min_price to 7. profit = 7 - 7 = 0: 
    No profit is made here.
max_profit = 0: No update needed.

Day 2(Price=1):

min_price = 1: The price 1 is smaller than the current min_price(7), so we update min_price to 1.
profit = 1 - 1 = 0: No profit is made.
max_profit = 0: No update needed.

Day 3(Price=5):

min_price = 1: The current price(5) is greater than the min_price(1), so no update to min_price. 
profit = 5 - 1 = 4: The profit if we bought at 1 and sold at 5 is 4.
max_profit = 4: Update max_profit to 4 since it’s higher than the current max profit(0).

Day 4(Price=3):

min_price = 1: The current price(3) is greater than min_price(1), so no update to min_price.
profit = 3 - 1 = 2: The profit is 2.
max_profit = 4: No update needed, as 4 is still the highest profit so far. 

Day 5(Price=6):

min_price = 1: The current price(6) is greater than min_price(1), so no update to min_price.
profit = 6 - 1 = 5: The profit if we sold at 6 is 5.
max_profit = 5: Update max_profit to 5 since it’s higher than 4.

Day6(Price=4):

min_price = 1: The current price(4) is greater than min_price(1), so no update to min_price.
profit = 4 - 1 = 3: The profit is 3.
max_profit = 5: No update needed, as 5 is still the highest profit.
FinalResult:
The function returns max_profit = 5, which is the maximum profit achievable by buying at 1 and selling at 6.
Output:

Maximum Profit: 5

"""

# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(18))


# import pandas as pd
#
# Student_details={
#     'std_id':[101,102,103,104,105],
#     'name':['Srinath','Akash','gokul','haroon','vishnu'],
#     'age':[21,22,22,21,22],
#     'grade':['A','A','A','A','A']
#
# }
# std_df=pd.DataFrame(Student_details)
# print(std_df[['name','grade']])


# nums = [1, 2, 3, 4]
#
#
# def li(nums):
#     l, r = 1, 1
#     n = len(nums)
#     l_a, r_a = [0] * n, [0] * n
#     for i in range(n):
#         j = -i - 1
#         l_a[i] = l
#         r_a[j] = r
#         l *= nums[i]
#         r *= nums[j]
#     return [l1 * r1 for l1, r1 in zip(l_a, r_a)]
#
#
# print(li(nums))


# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# merged = [(intervals[0])]
#
# print(merged[-1][1])
# print(intervals[1][1])
# # print(max(merged[-1][1]),intervals[1][1])
#
# print(max(merged[-1][1], intervals[1][1]))

"""
Given an m*n matrix, return all elements of the matrix in spiral order.

Example:
1:
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

"""

"""
def Spiral(matrix):
    m, n = len(matrix), len(matrix[0])
    i, j = 0, 0
    up, down, left, right = 1, 2, 3, 4
    ans = []
    up_wall = 0
    down_wall = m
    left_wall = -1
    right_wall = n
    direction = right
    while len(ans) != m * n:
        if direction == right:
            while j < right_wall:
                ans.append(matrix[i][j])
                j += 1
            i, j = i + 1, j - 1
            right_wall -= 1
            direction = down
        elif direction == down:
            while i < down_wall:
                ans.append(matrix[i][j])
                i += 1
            i, j = i - 1, j - 1
            down_wall -= 1
            direction = left
        elif direction == left:
            while j > left_wall:
                ans.append(matrix[i][j])
                j -= 1
            i, j = i - 1, j + 1
            left_wall += 1
            direction = up
        else:
            while i > up_wall:
                ans.append(matrix[i][j])
                i -= 1
            i, j = i + 1, j + 1
            up_wall += 1
            direction = right
    return ans


matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Spiral(matriz))
"""

"""
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

"""

1.Armstrong Number
2.Strong Number
3.Happy Number
4.xylem or phloem
5.Factorial
6.Prime Number
7.Reversing a number
8.Perfect Square
9.Perfect Number
10.Harshad Number
11.Fibonacci series

"""

# sum = 0
# a = 153
# n= len(str(a))
# a1 = a
# while a > 0:
#     temp = a % 10
#     sum += temp**n
#     a //= 10
# print(sum)
# if sum == a1:
#     print('Armstrong Number')
# else:
#     print('Not a Armstrong Number')


# sum = 0
# n = 40585
# n1 = n
# while n > 0:
#     temp = n % 10
#     fact = 1
#     while temp > 0:
#         fact *= temp
#         temp -= 1
#     sum += fact
#     n //= 10
# print(sum)
# if sum == n1:
#     print('Strong Number')
# else:
#     print('Not a Strong Number')


# l = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
# for n in l:
#     while n > 9:
#         sum = 0
#         while n > 0:
#             temp = n % 10
#             sum += temp**2
#             n //= 10
#         n = sum
#     if n == 1 or n == 7:
#         print('Happy Number')
#     else:
#         print('Not a Happy Number')

# 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100


# a = 1234
# a1 = a
# outer_sum = 0
# inner_sum = 0
# while a > 0:
#     temp = a % 10
#     if a == a1 or a < 10:
#         outer_sum += temp
#     else:
#         inner_sum += temp
#     a //= 10
#
# if outer_sum == inner_sum:
#     print('xylem number')
# else:
#     print('phloem number')


# def fa(n):
#     if n == 1:
#         return 1
#     return n * fa(n - 1)
#
#
# print(fa(6))

# n = int(input('enter a number:'))
# fact = 1
# while n > 0:
#     fact *= n
#     n -= 1
# print(fact)

# n = int(input('enter a number:'))
# if n < 2:
#     print('Not a prime number')
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             print('not a prime number')
#             break
#     else:
#         print('prime number')


# for i in range(2, 11):
#     for j in range(3, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')

# n = int(input('enter a number:'))
# sum = 0
# i = 1
# while i <= n // 2:
#     if n % i == 0:
#         sum += i
#     i += 1
# if n == sum:
#     print('perfect Number')
# else:
#     print('Not a perfect number')
#
# def p(n):
#     temp = n**0.5
#     if temp == temp // 1:
#         return 'perfect square'
#     else:
#         return 'not a perfect square'


# s = input('Enter the input:')
# d = {')': '(', '}': '{', ']': '['}
# stack = []
# for i in s:
#     if i not in d:
#         stack.append(i)
#     else:
#         if not stack:
#             print(False)
#         else:
#             popped = stack.pop()
#             if popped != d[i]:
#                 print(False)
# print(not stack)


# import mysql.connector
#
#
# s= mysql.connector.connect(
#     host='localhost',
#     user= 'root',
#     password= 'srinath',
#     database= 'scott'
# )
# print(s)
#
# query = '''INSERT INTO emp VALUES(1001,'SRINATH',20000
#
#          )'''
#
# c = s.cursor()
#
# c.execute(query)
# s.commit()

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# n = len(matrix)
#
# for i in range(n):
#     for j in range(i + 1, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# print(matrix)
#
# for i in range(n):
#     for j in range(n // 2):
#         matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
# print(matrix)


# ransomNote = "aa"
# magazine = "aab"
# m = {}
# for i in magazine:
#     if i in m:
#         m[i] += 1
#     else:
#         m[i] = 1
# print(m)

# for j in ransomNote:
#     if j not in m:
#         print(False)
#     elif m[j] == 1:
#         del m[j]
#     else:
#         m[j] -= 1
# print(not (not m))

# # text = "nlaebolko"
# text = "loonbalxballpoon"
# ballon = 'ballon'
#
# d = {}
# for i in text:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)
#
# if any(i not in d for i in ballon):
#     print(0)
# else:
#     print(min(d['b'], d['a'], d['l'] // 2, d['o'] // 2, d['n']))


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# d = {}
# for i in strs:
#     count = [0] * 26
#     for j in i:
#         count[ord(j) - ord('a')] += 1
#     key = tuple(count)
#     if key not in d:
#         d[key] = []
#     d[key].append(i)
# print([*d.values()])

# nums = [2, 2, 1, 1, 1, 2, 2]
#
# d = {}
# for i in nums:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# max_val = float('-inf')
# max_key = None
# for i,j in d.items():
#     if j > max_val:
#         max_val = j
#         max_key = i
# print(max_key)

# nums = [100, 4, 200, 1, 3, 2]
# s = sorted(nums)
# ans = []
# print(s)
# for i in range(len(s)-1):
#     if s[i+1] == s[i]+1:
#         ans.append(i)
# print(ans)
# s = "A man, a plan, a canal: Panama"
# s1 = s.split()
# res = ''
# print(s1)
# for i in s:
#     if i.isalnum():
#         res += i
# print(res)
# if res.lower() == res[::-1].lower(): print(True)
# else: print(False)


# n = int(input("enter a number:"))
# count = 1
# for i in range(n+1):
#     for j in range(i):
#         print(f'{count} ', end='')
#         count += 1
#     print()

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# n = len(height)
# left = 0
# right = n - 1
# max_a = 0
# while left < right:
#     wid = right - left
#     hei = min(height[left], height[right])
#     a = wid * hei
#     max_a = max(max_a, a)
#     if height[left] < height[right]:
#         left += 1
#     else:
#         right -= 1
# print(max_a)

# s = "(]"
# stack = []
# d = {')': '(', '}': '{', ']': '['}
# for i in s:
#     if i not in d:
#         stack.append(i)
#     else:
#         if not stack:
#             print(False)
#         else:
#             popped = stack.pop()
#             if popped != d[i]:
#                 print(False)
# print(not stack)
# print(d.values())
# print(d.keys())
# print(d.items())
#
# def fibo(num):
#     if num <= 1:
#         return num
#     else:
#         return fibo(num - 1) + fibo(num - 2)
#
#
# def print_ans(num):
#     count = 0
#     while count < num:
#         print(fibo(count), end=' ')
#         count += 1
#
#
# print_ans(10)

# def fib(num):
#     ans = [0, 1]
#     count = 0
#     if num == 1:
#         return ans[0]
#     else:
#         while count < num - 2:
#             ans.append(ans[-1] + ans[-2])
#             count += 1
#     return ans
#
#
# num = int(input('enter a number:'))
# print(fib(num))
# n = int(input('enter a number:'))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

"""

1.Armstrong Number
2.Strong Number
3.Happy Number
4.xylem or phloem
5.Factorial
6.Prime Number
7.Reversing a number
8.Perfect Square
9.Perfect Number
10.Harshad Number
11.Fibonacci series

"""


# num = int(input('enter a number:'))
# n = len(str(num))
# num1 = num
# res = 0
# while num > 0:
#     temp = num % 10
#     res += temp ** n
#     num //= 10
# print(res)
# if num1 == res:
#     print('armstrong number')
# else:
#     print('not an armstrong')

# num = int(input('enter a number:'))
# num1 = num
# res = 0
# while num > 0:
#     temp = num % 10
#     fact = 1
#     while temp > 0:
#         fact *= temp
#         temp -= 1
#     res += fact
#     num //= 10
# if num1 == res:
#     print('strong number')
# else:
#     print('Not a strong number')

# num = int(input('enter a number:'))
# while num > 9:
#     res = 0
#     while num > 0:
#         temp = num % 10
#         res += temp**2
#         num //= 10
#     num = res
# if num == 1 or num == 7:
#     print('Happy number')
# else:
#     print('not a happy number')

# num = int(input('enter a number:'))
# num1 = num
# o_sum = 0
# i_sum = 0
# while num > 0:
#     temp = num % 10
#     if num == num1 or num < 10:
#         o_sum += temp
#     else:
#         i_sum += temp
#     num //= 10
# if i_sum == o_sum:
#     print('xylem number')
# else:
#     print('phloem number')

# num = int(input('enter a number:'))
# fact = 1
# while num > 0:
#     fact *= num
#     num -= 1
# print(fact)

# def fac(num):
#     if num == 0:
#         return 1
#     return num * fac(num - 1)
#
#
# print(fac(4))

# n = int(input('enter a number:'))
# def prime(n):
#     if n < 2:
#         return False
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 return False
#         else:
#             return True
#
# def prin(n):
#     for i in range(n):
#         if prime(i):
#             print(i, end= ' ')
# prin(100)

# n = int(input('enter a number:'))
# n1 = n
# rev = 0
# while n > 0:
#     temp = n % 10
#     rev = rev*10 + temp
#     n //= 10
# print(rev)
# if rev == n1:
#     print('palindrome number')
# else:
#     print('Not a palindrome number')

# n = int(input('enter a number:'))
# n1 = 0
# i = 1
# while i <= n // 2:
#     if n % i == 0:
#         n1 += i
#     i += 1
# if n1 == n:
#     print('perfect number')
# else:
#     print('not a perfect number')


# nums = [3, 2, 4]
# target = 6
# d = {}
# for i, j in enumerate(nums):
#     d[j] = i
# for i, j in enumerate(nums):
#     y = target - j
#     if y in d and d[y] != i:
#         print([i, d[y]])
#         break

# nums1 = [1, 3]
# nums2 = [2, 4]
# res = sorted(nums1 + nums2)
# print(res)
# if len(res) % 2 == 0:
#     print((res[len(res)//2 - 1] + res[len(res)//2])/2)
# else:
#     print(res[len(res)//2])

# s = "the sky is blue"
# s1 = s.split()
# print(s1)
# s1.reverse()
# print(s1)
# print(' '.join(s1))

# s = "anagram"
# t = "nagaram"
# s1 = {}
# for i in s:
#     if i not in s1:
#         s1[i] = 1
#     else:
#         s1[i] += 1
# print(s1)
# t1 = {}
# for i in t:
#     if i not in t1:
#         t1[i] = 1
#     else:
#         t1[i] += 1
# print(s1 == t1)

