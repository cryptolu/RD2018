#! /usr/bin/env python3

################################################################################
# LACS, 2018, developped for the Researchers' Days 2018
# YLC, very heavily inspired by Daniel Feher's program
################################################################################

import sys
import random
import argparse
import subprocess
import os.path

# Parse command line options
parser = argparse.ArgumentParser(description = 'Generate transactions for the Blockchain game')
parser.add_argument('-p', type = int, default = 1, help = 'number of pages, default is 1')
parser.add_argument('-n', type = int, default = 48, help = 'number of stickers per page, default is 48')
parser.add_argument('-e', type = float, default = 0.1, help = 'faulty transaction probability, default is 0.1')
parser.add_argument('-c', action = 'store_true', help = 'automatically compile latex file into pdf, default is to not compile automatically')

args = parser.parse_args()

# Generate transactions
with open("transactions.dat", "w") as fh:
	for i in range(args.p*args.n):
		p = random.uniform(0, 1)
		if p < args.e:
			# generate random 4-digit number where one digit is a letter
			s = ''
			letter_pos = random.randint(0, 3)
			for j in range(4):
				if j == letter_pos:
					s += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
				else:
					s += random.choice('0123456789')
			# remove leading zeros
			for j in range(4):
				if s[0] != '0':
					break
				else:
					s = s[1:]
			fh.write("\\trans{{{}}}\n\n".format(s))
		else:
			num = random.randint(1, 9999)
			fh.write("\\trans{{{}}}\n\n".format(num))

# Compile
if args.c == True:
	subprocess.call(['pdflatex', os.path.join('..', 'src', 'transactions.tex')])
