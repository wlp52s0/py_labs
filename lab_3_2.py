'''
В первой строке записана последовательность натуральных чисел, 
разделённых пробелами. Во второй строке записано натуральное число P — степень, в 
которую требуется возвести числа из первой строки и вывести через пробел.
'''

x = [int(x) for x in input().split()]
deg = int(input())
for i in range(len(x)):
    print(x[i] ** deg, end=' ')
