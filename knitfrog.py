#!/usr/bin/env python
""" Comment out the R chunks of an Rnw file and output a .tex file """

import re
import argparse
import os.path
import sys

parser=argparse.ArgumentParser()
parser.add_argument("--infile", required = True )
parser.add_argument("--outfile", required = True)
parser.add_argument("--overwrite", dest="overwrite", action="store_true")
parser.add_argument("--nooverwrite", dest="overwrite", action="store_false")
parser.set_defaults(overwrite = False)
args=parser.parse_args()

if os.path.isfile(args.outfile) & args.overwrite==False:
    print "Use --overwrite to allow existing files to be overwritten"
    sys.exit(1)

chunkstart = re.compile(r'^\s*<<(.*)>>=.*$')
chunkend = re.compile(r'^\s*@\s*(%+.*|)$')
inlineCode = re.compile(r'(\\Sexpr)(\{.+\})')


inchunk = False
with open(args.infile, mode="r") as infile:
    with open(args.outfile, mode="w") as outfile:
        for line in infile:
            outline = inlineCode.sub(r"\\texttt\2", line)
            
            if chunkstart.match(line):
                inchunk = True
            if inchunk == True:
                outline = "% " + outline
            if chunkend.match(line):
                inchunk = False
            outfile.write(outline)
                

