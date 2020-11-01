#-*-    coding:utf-8    -*-
'''
用生成器实现斐波那契前n项数列
'''
def fib_generator(n):
    num1,num2=0,1
    try:    #异常值检测
        while n>0:
            yield num1
            num1,num2=num2,num1+num2
    except StopIteration:
        pass

while True:
    terms=input("请输入项数：")    
    if not terms.isdigit():    #判断输入是否符合要求
        print("输入有误，请输入一位正整数")
    else:
        n=int(terms)
        print(f'斐波那契前{n}项数列为:')
        result=fib_generator(n)
        for _ in range(n):    #_是占位符
            print(next(result),end=' ')    #只有调用next()函数 才会运行函数中代码
        break

