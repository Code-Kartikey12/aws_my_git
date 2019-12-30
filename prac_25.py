#!/bin/python3

import math
import os
import random
import re
import sys

print("Enter a number ")
input_num = int(input())
print(f"input number: {input_num}")
if input_num % 2 == False:
    if input_num > 2 and input_num < 5:
        print("Not Weird")
    elif input_num > 6 and input_num < 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")