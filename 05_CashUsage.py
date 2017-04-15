#!/usr/local/bin/python3.5

input='''15
HCNQFS30 200
EBOJVX04 6600
LVDSYF60 1300
LTBTDD36 300
CPUQVQ02 1200
HCNQFS30 5300
LTBTDD36 10000
CPUQVQ02 6000
YYWOFA55 3400
YYWOFA55 200
EBOJVX04 7300
CPUQVQ02 8500
LVDSYF60 3800
HCNQFS30 7100
LTBTDD36 2900'''

lines = input.split("\n")
accounts = {}

for i in range(1, int(lines[0])+1):
        account, cash = lines[i].split(" ")
        if account not in accounts:
                accounts[account] = int(cash)
        else:
                accounts[account] += int(cash)

items = [(acc, val) for (acc, val) in accounts.items()]
items.sort(key=lambda x:x[1])
answer = (acc for acc, val in items)
for i in answer:
        print(i, end=' ')
