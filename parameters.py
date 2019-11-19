# def wish(name="Guest",msg):        #pass #SyntaxError: non-default argument follows default argument
# def wish( msg,name="Guest"): pass  #valid

#variable lenth aruguments
# def sum(a,b):
#     print(a+b)
# def sum(a,b,c):
#     print(a+b+c)
#
# sum(10,20,30)
# sum(10,20)
# def f1(*n):   #any number of arguments
#     print("var-arg function")
# f1()
# f1(10)
# f1(10,20)
# f1(10,20,30)
# f1(10,20,30,40)
# WAP to print of given sum numbers
# def sum(*n):
#     result=0
#     for x in n:
#         result=result+x
#     print("The sum:",result)
#
# sum()
# sum(10)
# sum(10,20)
# sum(10,20,30)
# def display(**x):
#     print(type(x))
#     for k,v in x.items():
#         print(k,"....",v)
# display(name="raju",marks=100,age=23,gf="san")
# display(name="kumar",wife="sruhi",age=23,gf="san")
#
def f1(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f1(3,2)
f1(10,20,30,50)
f1(25,30,arg4=100)
f1(arg4=2,arg1=3,arg2=4)
# f1()#TypeError: f1() missing 2 required positional arguments: 'arg1' and 'arg2'
# f1(arg3=10,arg4=40,20,30)#SyntaxError: positional argument follows keyword argument
# f1(4,5,arg2=6) #TypeError: f1() got multiple values for argument 'arg2'
f1(4,5,arg4=0,arg6=2)#TypeError: f1() got an unexpected keyword argument 'arg6'
