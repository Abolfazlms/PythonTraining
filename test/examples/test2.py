import datetime as dt
import copy 

def Test():
    # number = 100;
    # result = number*(number+1)/2
    # return print(int(result))

    calendar = dt.datetime.now()
    print("%s-%s-%s %s:%s"%(calendar.year,calendar.month,calendar.day,calendar.hour,calendar.minute))
    print("{0}-{1:02}-{2:02} {3:02}:{4:02}".format(calendar.year,calendar.month,calendar.day,calendar.hour,calendar.minute))
    print(f"{dt.datetime.now():%Y-%m-%d %H:%M}");

    
    # testStr = 'This is a test string'
    # testStr2 ='AlphaString'
    #print(testStr.strip('Tgnh.'))
    #print(testStr.center(3,'*'))
    #print(testStr.count('test'))
    # print(testStr.endswith('.'))
    # print(testStr.split(' '))
    # print(testStr.replace('test','new'))
    # print(testStr.upper())
    # print(testStr2.isalpha())
    
    # byteStr = b'Python Byte Text'
    # print(byteStr)
    # print(byteStr.decode('UTF-8'))
    # byteArrayStr = bytearray(byteStr)
    # print(byteArrayStr)
    # byteArrayStr[0] = 82
    # print(byteArrayStr.decode('utf-8'))

    # list1 = [1,2,3,21,9,43]
    # print(list1[:len(list1)-2])
    # print(list1[3][0])
    #list1[1:1]=[5,6,7]
    #del list1
    # print(list1)    
    # list2 = copy.copy(list1)
    # list3 = copy.deepcopy(list1)
    # list1[0] = 2
    # print(f'list1 is{list1}\nand List2 is {list2}\nand List3 is {list3}')
    # print(3*list1+['Hello'])
    # list1.append(['hello'])
    # list1.extend(['python'])
    # list1.extend('python')
    # list1.remove(['hello'])
    # print(list1.pop(2))
    # list1.pop()
    # print(list1.index('p'))
    # print(list1.count(1))
    #list1.clear()
    # print(list1.reverse())
    # print(list1.sort(reverse = True))
    # print(sorted(list1))
    # print(list1)

    # stack = []
    # stack.append(1)
    # stack.append(2)
    # stack.append(3)
    # stack.pop()
    # print(stack)

    # tuple1 = (1,2,3,4)
    # tuple2 = 5,6,[7,8]
    # tuple3 = (9,)
    # tuple4 = ('d','h','f','e','g')
    # tuple2[0] = 1
    # tuple2[2][0]=8
    # print(tuple1 + (2 * tuple2) + tuple3)
    # a,b,*c = tuple1 + (2 * tuple2) + tuple3
    # print(a,b,c)
    # tuple1 = list(tuple1)
    # tuple1[0] = 21
    # tuple1 = tuple(tuple1)
    # print(tuple1)
    # tuple4 = sorted(tuple4, key = str.upper, reverse = True)
    # print(tuple4)
    