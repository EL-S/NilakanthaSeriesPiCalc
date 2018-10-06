from decimal import *
getcontext().prec = 100000

pivalue = 3 # starts with 3
c=0
denominator = 1
plusminus = 0

for i in range(1,100000):
    denominator = (i*2) * ((i*2)+1) * ((i*2)+2)
    print(denominator)
    if plusminus == 0:
        pivalue += Decimal(4)/Decimal(denominator)
        denominator = 1
        plusminus = 1
    else:
        pivalue -= Decimal(4)/Decimal(denominator)
        denominator = 1
        plusminus = 0

print(pivalue)
