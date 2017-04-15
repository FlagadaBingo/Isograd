#!/usr/local/bin/python3.5

import time

input='''5
1 8
2 3
4 23
4 6
2 23'''


def calcul_temps(fonction):
        def wrapper():
                avant = time.time()
                fonction()
                apres = time.time()
                print(apres - avant)
        return wrapper


@calcul_temps
def horaires1():
        hours = {}
        for time in range(1,25):
                hours[time] = 0

        def inBetween(line):
                current = int(line.split(" ")[0])
                while current < int(line.split(" ")[1]):
                        hours[current] +=1
                        current += 1
        list(map(inBetween, input.split("\n")[1:]))
        print(hours)
        return 0


@calcul_temps
def horaires2():
        lines = input.split("\n")
        hours={}
        for time in range(1,25):
                hours[time] = 0

        for i in range(1, int(lines[0])+1):
                start, stop = lines[i].split(" ")
                for heure in range(int(start), int(stop)):
                        hours[heure] += 1
        print(hours)
        return 0


horaires1()
horaires2()
