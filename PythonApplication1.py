'''
a=10
b=20
if a>b:
    print('a为最大数')
else:
    print('b为最大数')
'''
'''
i=1
sum=0
while(i<=100):
    sum=sum+i
    i=i+1
else:
    print('等差数列一到一百的和') #python有别于c的不同 while...else语句
print(sum)
'''
'''
#无限循环
a=1
while(a):
    print('hello world')#ctrl+c结束无限循环

print('good bye!')#输出结果并没有执行这个语句
'''
'''
#for语句
a=[1,2,3,4,5,6]
for i in a:
   print(i,end='')
'''
   #range()函数会生成数列
for i in range(10):#从零开始十个数
    print(i)
for b in range(1,8):#不包含8
    print(b)
print('\n')
for a in range(1,20,5):#也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'): 
    print(a)#range(开始位置，结束位置，步长）

#使用range()函数来创建一个列表
a=list(range(9))
print(a)

#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

#continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。 
'''
pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句，如下实例
实例
>>>while True:
    pass  # 等待键盘中断 (Ctrl+C)
'''