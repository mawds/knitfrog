# knitfrog
Scripts to (un)comment Knitr chunks in Rnw documents

[Knitr](https://yihui.name/knitr/) provides "Elegant, flexible and fast dynamic report generation with R".   Occasionally it can be useful to just focus on the LaTeX source, and not worry about the R code.  For example, if working on a project that requires a live internet connection when working offline.

This script automates the (un)commenting of the code chunks, and outputs a tex file, which can then be compiled with, e.g. pdflatex.

The name comes from "frogging", which apparently is the term used by knitters when they undo their knitting (http://www.knitty.com/ISSUEwinter03/FEATwin03TT.html)
