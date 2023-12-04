#Thank Jonathan Pauslson!
#https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py

import sys

#!/usr/bin/python3
import argparse
import subprocess
import sys
import requests

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.
SESSION = '53616c7465645f5f8eaf5e34ae75dbe6f9cb6f0ed2d61f40b5f09e527947722d7d1da15fea0654738f50dd949f124dfce9334ed473023f282e14ab5c39a561e3'

useragent = 'https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py by jonathanpaulson@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2022)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

#Had to remove useragent to make sure this command works fine
cmd = f'curl.exe https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}"'
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)