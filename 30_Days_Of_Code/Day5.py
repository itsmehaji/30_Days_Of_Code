#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
result=n*1
for i in range(1,11):
    result=n*i
    print(n,'x',i,'=',result)
