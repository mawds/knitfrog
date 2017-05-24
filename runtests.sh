#!/bin/bash
rm tests/testdoc.*
./knitfrog.py --infile testdoc/testdoc.Rnw --outfile tests/testdoc.tex
diff tests/testdoc.tex testdoc/testdoc.tex
exit_status=$?
if [ $exit_status -ne 0 ]
    then
    echo "*** Conversion to tex failed"
fi


./knitfrog.py --infile testdoc/testdoc.Rnw --outfile tests/testdoc.tex

exit_status=$?
if [ $exit_status -ne 1 ]
    then
    echo "*** Overwrite test failed"
fi

./knitfrog.py --infile tests/testdoc.tex --outfile tests/testout.Rnw
diff testdoc/testdoc.Rnw tests/testout.Rnw


exit_status=$?
if [ $exit_status -ne 0 ]
    then
    echo "*** Could not convert file back"
fi