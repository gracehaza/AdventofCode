import math

filepath = 'day01.txt'

fuel = 0 

def domath(input):
    stepone = float(input/3)
    steptwo = math.floor(stepone)
    stepthree = steptwo -2
    if stepthree > 0:
        global fuel
        fuel = fuel + stepthree
        domath(stepthree)
        print("running total: {}\n".format(fuel))

with open(filepath,"r") as filenow:
    lineslist = filenow.readlines()
    for i in range(0,len(lineslist)):
        print(i)
        print(lineslist[i])
        numberstring =  lineslist[i]
        number = float(numberstring)
        domath(number)
