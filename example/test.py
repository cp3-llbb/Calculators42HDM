#!/usr/bin/python

import math
from cp3_llbb.Calculators42HDM.Calc2HDM import *

# Alex's PhD thesis parameters
mode = 'H'
sqrts = 13000
type = 2
mh = 125
mH = 500
mA = 300
tb = 1.5
cba = 0.01
sba = math.sqrt(1 - pow(cba, 2))
mhc = max(mH, mA)
m12 = math.sqrt(pow(mhc, 2) * tb / (1 + pow(tb, 2)))
outputFile = "out.dat"


test = Calc2HDM(mode = 'H', sqrts = sqrts, type = type, tb = tb, m12 = m12, mh = mh, mH = mH, mA = mA, mhc = mhc, sba = sba, outputFile = outputFile)
test.computeBR()


#print "ZZ BR", test.HtoZZBR
print "m12: ", test.m12
print "H width: ", test.Hwidth 
print "A width: ", test.Awidth 
print "lambda_1 ", float(test.lambda_1)
print "lambda_2 ", float(test.lambda_2)
print "lambda_3 ", float(test.lambda_3)
print "lambda_4 ", float(test.lambda_4)
print "lambda_5 ", float(test.lambda_5)
print "lambda_6 ", float(test.lambda_6)
print "lambda_7 ", float(test.lambda_7)

#xsec = test.getXsecFromSusHi()
#print "xsec : ", xsec


#test.setmA(200)
#test.computeBR()
#print "ZZ BR second test", test.HtoZZBR
#print "H width: ", test.Hwidth 
