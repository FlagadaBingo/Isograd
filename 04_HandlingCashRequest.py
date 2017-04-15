#!/usr/local/bin/python3.5

input='''26639
15
1
402
1982
6459
14886
15588
16784
17214
17720
19111
19552
31958
33911
40922
44958'''

cash=int(input.split("\n")[0])
delivery={}
while cash !=0:
        bill=int(max(filter(lambda x:x<=cash,map(int, input.split("\n")[2:]))))
        cash -= bill
        if bill in delivery: delivery[bill] += 1
        else: delivery[bill] = 1

list(map(lambda x:print(str(x)+' '+str(delivery[x])), sorted(delivery, reverse=True)))
