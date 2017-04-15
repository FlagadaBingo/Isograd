#!/usr/local/bin/python3.5

input='''
8
6536808952049258
3050888190221805
4342421941443910
1778669572780861
1662857991393098
8647110900764965
9916918201302186
6517517683080242
'''

for card in range(2, int(input.split("\n")[1])+2):
        res=0
        for rang, numb in enumerate(input.split("\n")[card]):
                if rang < 15:
                        if rang % 2 == 0 :
                                if int(numb)*2 > 9 : res+=int(numb)*2 - 9
                                else : res+=int(numb)*2
                        else :res+=int(numb)
                else :
                        if (res + int(numb))%10 == 0: print(res)
                        else: pass
