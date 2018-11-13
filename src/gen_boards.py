#! /usr/bin/env python3

################################################################################
# LACS, 2018, developped for the Researchers' Days 2018
# YLC, very heavily inspired by Daniel Feher's program
################################################################################

import sys
import random
import subprocess
import argparse


def output_header(fh):
	header = r"""\documentclass{article}
	\usepackage[utf8]{inputenc}
	\usepackage{graphicx}
	\usepackage{hhline}
	\usepackage{amsmath}
	\usepackage{amssymb} % for \ulcorner
	\usepackage{caption}
	\usepackage{rotating}
	\usepackage{multirow}
	\usepackage[landscape]{geometry}
	\geometry{left=0mm,right=0mm,top=0mm,bottom=0mm}
	\usepackage{tabularx}
	\newcolumntype{Y}{>{\centering\arraybackslash}X}
	\captionsetup[table]{labelformat=empty}
	\newcommand{\phs}{\raisebox{-5pt}{\framebox(30, 25){}}\hspace{10pt}}
	\newcommand{\phd}{\underline{\hspace{30pt}}\hspace{10pt}}
	\newcommand{\phe}{\hspace{40pt}}
	\begin{document}
	"""
	fh.write(header)


def output_page_header(fh, seed):
	page_header1 = r"""
	\clearpage
	\newpage
	\pagestyle{empty}
	\begin{table}
		\Huge
		\centering
		\begin{tabularx}{0.95\textwidth}{|Y|c|}
			\hline
			Transactions & Hash calculation \\
			\hline
			& {
				\begin{tabular}{lrr}
					\\
					1. & Prev block:      &       \phe \phe \phe \phd \phd \\
					2. & Transaction sum: &  ~~+~ \phd \phd \phd \phd \phd \\
					3. & Total sum:       &  ~~=~ \phd \phd \phd \phs \phs \\
					\\
					4. & \multicolumn{2}{c}{
						\huge
						\begin{tabular}{|c|c||c|c|c|c|c|c|c|c|c|c|}
							\cline{3-12}
							\multicolumn{2}{c|}{} & \multicolumn{10}{c|}{Second digit} \\
							\cline{3-12}
							\multicolumn{2}{c|}{\small{"""

	page_header2 = r"""}} & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
							\hhline{--*{10}{|=}|}
							\multirow{10}{*}{\begin{sideways}First digit\end{sideways}}
	"""
	fh.write(page_header1)
	fh.write("ID: 0x{:04x}".format(seed))
	fh.write(page_header2)


def output_page_footer(fh):
	page_footer = r"""\hline
						\end{tabular}
						} \\
					\\
					5. & Hash:          & \multicolumn{1}{l}{\phd \phd} \\
					6. & Signature:     & \multicolumn{1}{l}{\underline{\hspace{200pt}}} \\
				\end{tabular}
			}
			\\
			\hline
		\end{tabularx}
	\end{table}
	"""
	fh.write(page_footer)
	

def output_footer(fh):
	footer = r"""\end{document}"""
	fh.write(footer)


def output_values(fh, values):
	for row_idx in range(10):
		line = "& " + str(row_idx) + "&" + " & ".join(values[10*row_idx:10*row_idx + 10]) + " \\\\"
		if row_idx != 9:
			line += "\cline{2-12}"
		line += '\n'
		fh.write(line)


################################################################################
# Main
################################################################################

# Parse command-line options
parser = argparse.ArgumentParser(description = 'Generate boards for the Blockchain game')
parser.add_argument('-p', type = int, default = 1, help = 'number of look-up tables, default is 1')
parser.add_argument('-n', type = int, default = 6, help = 'number of boards per look-up table, default is 6')
parser.add_argument('-o', type = str, default = "boards", help = "base name of output files (.tex and .pdf added at the end automatically), default is 'board'")
parser.add_argument('-c', action = 'store_true', help = "compile latex to pdf automatically, default is to not compile automatically")

args = parser.parse_args()
tex_filename = args.o + ".tex"

# Generate latex file
with open(tex_filename, "w") as fh:
	output_header(fh)
	for lookup_idx in range(args.p):
		values = [str(i) for i in range(100)]
		seed = random.getrandbits(16)
		random.seed(seed)
		random.shuffle(values)
		for board_idx in range(args.n):
			output_page_header(fh, seed)
			output_values(fh, values)
			output_page_footer(fh)
	output_footer(fh)

# Compile
if args.c == True:
	subprocess.call(['pdflatex', tex_filename])
