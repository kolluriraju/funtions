# s=lambda a,b:a+b
# print("the sum of {} and {} is: {}".format(2,4,s(2,4)))
# s=lambda n:n*n
# print(s(5))

# s=lambda a,b:a if a>b else b
# print("The Biggest of 10,20 is:",s(10,20))
# print("The Biggest of 100,200 is:",s(100,200))
#  #The Biggest of 10,20 is: 20
# # The Biggest of 100,200 is: 200
# 1.filter():
# def iseven(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l=[1,2,3,4,5,6,7,8,9,10]
# l1=list(filter(iseven,l))
# print(l1)
# l=[0,5,10,20,30,50,45,30]
# l1=list(filter(lambda x:x%2==0,l))
# print(l1)
# l1=list(filter(lambda x:x%2!=0,l))
# print(l1)
# l=[0,5,10,15,20,25,30]
# l1=[0,10,20,30,40,50,60]
# # l2=list(map(lambda x:x*x,l1))
# l2=list(map(lambda x,y:x*y,l,l1))
# print(l2)
# l1=[1,2,3,4,10]  #ignored more elements in map function
# l2=[2,3,4,5]  #must equal to two lists in map function
# l3=list(map(lambda x,y:x*y,l1,l2))
# print(l3)

# reduce() rduces sequence of elements single elemnts converted to single value one value
# from functools import reduce
#
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x+y,l)
# print(result)
# def wish(name):
#     print("Good morning:",name)
# greating=wish
# print(id(wish))
# print(id(greating))
# wish("Raju")
# greating("srishalam")
# del wish
# # wish("kumar")
# greating("sri")
# Nested Function
# def outer():
#     print("outer function started")
#     def inner():
#         print("inner function excution")
#     inner()
# outer()
# def f1():
#     def inner(a,b):
#         print("the sum:",a+b)
#         print("the avg:",(a+b)/2)
#     inner(10,20)
#     inner(20,30)
#     inner(100,200)
# f1()
#inner() #not possible outside the function
# to define function specific repatedly required functionality
def outer():
    print("outer function started")
    def inner():
        print("inner function excuted")
    print("outer function retuerning inner function")
    return inner
f1=outer()
f1()
