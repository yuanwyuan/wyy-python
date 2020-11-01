#-*-    coding:utf-8    -*-
'''
用递归法实现斐波那契前n项数列
'''
def fib_recur(n): 
    if n <= 1:    #如果n为0或1，则返回它本身   
    	return n
    elif n == 2:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)    #通项公式F(n) = F(n-1) + F(n-2)

while True:
    terms=input("请输入项数：")    
    if not terms.isdigit():    #判断输入是否符合要求
        print("输入有误，请输入一位正整数")
    else:
        n=int(terms)
        print(f'斐波那契前{n}项数列为:')
        for i in range(0, n):    #生成前n项数列
            print(fib_recur(i), end=' ')
        break

