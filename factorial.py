# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
L = [2,3]
n = int(input())
k = 4

while k>0:
      if len(L) == n:
             break
for i in L:
 if k%i==0:
  break
 else:
     L.append(k)
     k+=1
 print(L[-1])