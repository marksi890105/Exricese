# #!/usr/bin/python3
# # -*- coding=utf-8 -*-


#
# letters = ['a','b','c','d','e','f']
# print(letters)
# letters[2:5] = ['D','E',]
# print(letters)
# # now remove them
# letters[2:5] = []
#
# print(letters)
# # clear the list by replacing all the element with an empty list
# letters[:] = []
#
# print(letters)
#

#
# letters = ['a','b','c','d','f']
#
# len(letters)
#
# print(letters)
#
# a = ['a','b','c']
# n = [1,2,3]
# x = [a, n]
# print(x)
#
# print(x[0])
# print(x[1])
# print(x[0][1])
#
# # Fibonacci series :
# # the sum of tow elments defines next
# a, b = 0,1
# while a <  10:
# #     print(a)
# #
#
# # i = 256*256
# # print('The value of i is',i)
#
# # a, b = 0, 1
# # while a < 1000:
# #     print(a, end=',')
# #     a, b = b, a+b
# #
#
#
#
# # # measure some strings:
# # words = ['cat','window','defenestrate']
# # for w in words:
# #     print(w,len(w))
# #
#
# strategy iterate over a copy
# for user; status in users.copy() . items():
#     if status == "inactive":
#         del users[user]
#
# # strategy create a new collection
# active_users = {}
# for user, status in users,items():
#     if status == 'active'
#         active_users[user] = status
#
#
#


# for i in range(5):
# # #     print(i)
# # #


# a = ['mary','had','a ','little','lamb']
# for i in range(len(a)):
#     print(i,a[i])

#
# a = range(4)
#
# b = list(range(4))
#
# # print(list(b
#
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n,'equal',x,'*',n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n,'is a prime number')
#


# for num in range(2,10):
#     if num % 2 == 0:
#         print('Found an even number', num)
#         continue
#     print("Found a number", num)

# while True:
#     pass # Busy-wait for keyword interrupt (Ctrl+C)


# class MyEmptyClass:
#     pass

# def initlog(*args)
#     pass #Remember to implement this !

#
# def fib(n): # write Fibonacci series up to n
#     """Print a Fibonacci series up to n,"""
#     a, b = 0, 1
#     while a < n:
#         print(a,end=' ')
#         a, b = b, a+b
#     print()
# #Now call the funcation we just defined:

# def Fib2(n):   # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n """
#     result = []
#     a, b  = 0, 1
#     while a < n:
#         result.append(a) # see blow
#         a, b  = b, a+b
#         return result
#     f100  = fib2(100) # call it
#             # write the result


# def ask_ok(prompt,retries=4, reminder='please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y','ye','yes'):
#             return True
#         if ok in ('n','no','nop',):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('Invalid user response')
#         print(remin


#
# i = 5
# def f(arg=i):
#     print(arg)
#
#
# i = 6
# print(f)
#


# def f(a, L=[]):
#      L.append(a)
#      return L
#
# print(f(1))
# print(f(2))
# print(f(3))


# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
#
# def parrot(voltage,stat='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put ",voltage,"volts through it.")
#     print("--Lovely plumage, the", type)
#     print("-- It's", state,"!" )
#
#
#
# parrot(1000)               # 1 positional argument
# parrot(voltage=1000)        # 1 keyword argument
# parrot(voltage=1000000,  action='V00000M')
# parrot(action='V00000M', voltage=1000000)
# parrot(a million ,'bereft of life','')
#

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any",kind, "?")
#     print("--I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":",keywords[kw])
#
#
# cheeseshop("limburger","It's very runny, sir.",
#            "It's really very, VERY runny, sir,",
#            shopkeeper="Michael Palin",
#            client="John cheese",
#            sketch="Cheese Shop Sketch")

# def standard_arg(arg):
#     print(arg)
#
# def pos_only_arg(arg, /):
#     print(arg)
#
# def kwd_only_arg(*, arg):
#     print(arg)
#
#
# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)
#
#
# def foo(name, **kwds):
#     return 'name' in kwds
#

# def foo(name, /, **kwds):
# # # # #     return 'name' in kwds
# # # # #     foo(2,**{'name': 2})

# list(range(4, 6))
# print(list)
#
# arg = [4, 6]
# list(range(*arg))
# arg2 = list(range(*arg))
# print(arg2)

#
# def parrot(voltage, stat='a stiff', action='voom'):
#     print("--This parrot wouldn't", action, end=' ')
#     print("If you put ", voltage, "volts through it ", end=' ')
#     print("E s", stat, "!")
#
# d = {"voltage": "four million", "state" : "bleedin' demised", "action": "VOOM"}
# parrot2 = parrot(**d)
# print(parrot2)
# d = {'votalge'} :"four million",'state' :
import pymongo

print("welcome to python")print("welcome to python")"welcome to python")
# #!/usr/bin/python3
# # -*- coding=utf-8 -*-