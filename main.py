#!/usr/bin/python3

from useful_package import polynom_3
from useful_package import hyperbola

import argparse

parser = argparse.ArgumentParser(description="Return input variable x, cube of x and 1 / x.")
parser.add_argument('x', type=float,
                    help='a floating point value for calculating functions')

args = parser.parse_args()

x = args.x
print(x)
print(polynom_3(x))
print(hyperbola(x))
