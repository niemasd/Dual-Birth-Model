#!/bin/bash

tmpa=`mktemp XXXX`
tmpf=`mktemp XXXX`

cat - | tee >( nw_distance -sf -mp - > $tmpf )| nw_distance -sa -mp - |sed '$ d' >$tmpa

echo "
l = mean(read.csv('"$tmpf"',sep= ' ',header=F)\$V1)
b = mean(read.csv('"$tmpa"',sep= ' ',header=F)\$V1)
cat( if ( b > l) 1 else  ( 3 - 2 * b / l - 2 * sqrt(2*(1-b/l)) ) )
" | R --vanilla -q --slave

echo

rm $tmpf $tmpa 
