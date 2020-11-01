#-*-    coding:utf-8    -*-
'''
用矩阵实现斐波那契前n项数列
'''
import numpy as np
def fib_matrix(n):
    fib_mat = np.array([[1,0]])
    A_mat = np.array([[1,1],[1,0]])
    for i in range(n):
        if i == 0:
            print(fib_mat[0][1],end=' ')
        else:
            fib_mat=fib_mat.dot(A_mat ** n)    #两个矩阵的内积
            print(fib_mat[0][1],end=' ')

if __name__ == '__main__':
    while True:
        terms=input("请输入项数：")    
        if not terms.isdigit():    #判断输入是否符合要求
            print("输入有误，请输入一位正整数")
        else:
            n=int(terms)
            print(f'斐波那契前{n}项数列为:')
            fib_matrix(n)
        break
