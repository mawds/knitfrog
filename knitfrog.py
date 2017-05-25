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

if os.path.isfile(args.outfile) and args.overwrite==False:
    print "Use --overwrite to allow existing files to be overwritten"
    sys.exit(1)

chunkstartregex = r'\s*<<(.*)>>=.*$'
chunkendregex = r'\s*@\s*(%+.*|)$'

commentstring = "% "
# inlinetags = (r'\\Sexpr', r'\\texttt')
# We define the Sexpr command below this if need be
documentstring = r"\\documentclass\{"
commandstring = r"\newcommand{\Sexpr}[1]{\texttt{#1}}"
inext = os.path.splitext(args.infile)[1]
outext = os.path.splitext(args.outfile)[1]

KtoT = None # Knitr to Tex indicator
if inext == ".Rnw" and outext == ".tex":
    print "Commenting out Knitr chunks"
    chunkstart = re.compile("^" + chunkstartregex)
    chunkend = re.compile("^" + chunkendregex)
    KtoT = True

elif inext == ".tex" and outext == ".Rnw":
    print "Reinstating Knitr chunks"
    chunkstart = re.compile("^" + commentstring + chunkstartregex)
    chunkend = re.compile("^" + commentstring + chunkendregex)
    KtoT = False

else:
    print "Unrecognised extensions"
    sys.exit(1)

if KtoT is None:
    print "Conversion direction not set"
    sys.exit(1)


inchunk = False
with open(args.infile, mode="r") as infile:
    with open(args.outfile, mode="w") as outfile:
        for line in infile:
            # if KtoT == True: 
            #     outline = re.sub("(" + inlinetags[0] + r")(\{.+\})",
            #         inlinetags[1] + r"\2", line)
            # else:
            #     outline = re.sub("(" + inlinetags[1] + r")(\{.+\})",
            #         inlinetags[0] + r"\2", line)
            outline = line
            if re.match(documentstring, outline) and KtoT is True:
                outfile.write(outline)
                outfile.write(commandstring)
                continue
            if KtoT is False and outline.rstrip() == commandstring:
                print "deleting commandstring"
                continue
            if chunkstart.match(line):
                inchunk = True
            if inchunk == True:
                if KtoT == True:
                    outline = commentstring + outline
                else:
                    outline = re.sub("^" + commentstring + "(.+$)", r"\1", 
                        outline)
            if chunkend.match(line):
                inchunk = False
            outfile.write(outline)
    

