#!/usr/bin/env python
""" Comment out the R chunks of an Rnw file and output a .tex file """

import re
import argparse
import os.path
import sys

parser=argparse.ArgumentParser()
parser.add_argument("infile")
parser.add_argument("--outfile", required=False)
args=parser.parse_args()


chunkstart = re.compile(r'^\s*<<(.*)>>=.*$')
chunkend = re.compile(r'^\s*@\s*(%+.*|)$')
inlineCode = re.compile(r'(\\Sexpr)(\{.+\})')

if args.outfile is not None:
    outfile = args.outfile
else:
    outfile = os.path.splitext(args.infile)[0] + ".tex" 

inchunk = False
with open(args.infile, mode="r") as infile:
    with open(outfile, mode="w") as outfile:
        for line in infile:
            outline = inlineCode.sub(r"\\texttt\2", line)
            
            if chunkstart.match(line):
                inchunk = True
            if inchunk == True:
                outline = "% " + outline
            if chunkend.match(line):
                inchunk = False
            outfile.write(outline)
                

