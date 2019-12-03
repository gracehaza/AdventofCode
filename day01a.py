import math

filepath = 'day01.txt'

with open(filepath,"r") as filenow:
    lineslist = filenow.readlines()
    fuel = 0
    for i in range(0,len(lineslist)):
        print(i)
        print(lineslist[i])
        numberstring =  lineslist[i]
        number = float(numberstring)
        print ("number: {}".format(number))
        stepone = float(number/3)
        print ("step one: {}".format(stepone))
        steptwo =  math.floor(stepone)
        print ("step two: {}".format(steptwo))
        stepthree = steptwo - 2
        print ("step three: {}".format(stepthree))
        fuel = fuel + stepthree
        print("running total: {}\n".format(fuel))
