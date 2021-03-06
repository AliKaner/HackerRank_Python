import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
#---------------------------------------------
    if (n%2 == 0 and (n>20 or n<6) ):
        print("Not", end =" ")
    print("Weird")
#---------------------------------------------