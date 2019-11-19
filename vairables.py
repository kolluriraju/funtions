# types of varibles
# 1.Global variable=====out side the function
# 2.Local varibale====== in side the function
# a=10
# def f1():
#     print("f1:",a)
# def f2():
#     print("f2:",a)
# f1()
# f2()
# a=10
# def f1():
#     global a   # inside the function gobal using
#     a=777         #local variables
#     print("f1:",a)
# def f2():
#     print("f2:",a)
# f2()
# f1()    # local
# f2()              # NameError: name 'a' is not defined
# a=10
# def f1():
#     a=20
#     print(a)
#     print(globals()['a'])
# f1()
def f1():
    a=10
    global a   #SyntaxError: name 'a' is assigned to before global declaration
    a=50
    print(a)
f1()