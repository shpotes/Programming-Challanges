# UVA - 11112 / Babylonian Roulette
# Ad hoc

import math
while(True):
    p0, b, pf = map(int, input(). split())
    if(p0 + b + pf == 0):
        break
    if((pf - p0) % b):
        print("No accounting tablet")
    else:
        foo = abs(pf - p0)/b
        print(math.ceil(foo/3))
