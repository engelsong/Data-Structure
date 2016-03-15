import time
import random

def CalTimeCost(name, *arg):
    start = time.time()
    sum1 =  name(arg)
    stop = time.time()
    return stop - start



