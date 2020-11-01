#-*-    coding:utf-8    -*-
'''
用循环法实现斐波那契前n项数列
'''
def fib_circle():
    while True:
        terms=input("请输入项数：")    
        if not terms.isdigit():    #判断输入是否符合要求
            print("输入有误，请输入一位正整数")
        else:
            n=int(terms)-1    #列表里已经有第一个0初始值，所以这里输入数目减一
            num1,num2 = 0,1    #设置初始值
            fib_seq=[0]    #用列表存储生成的数据
            for i in range(n):
                num1,num2 = num2,num1+num2    #更新数据
                fib_seq.append(num1)
            print(f'斐波那契前{n+1}项数列为:')    #用户输入的数据比n多一位，这里要加一
            print(fib_seq)
            break

if __name__ =="__main__":
    fib_circle()
