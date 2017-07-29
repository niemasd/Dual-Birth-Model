#!/bin/bash

tmpa=`mktemp XXXX`
tmpf=`mktemp XXXX`

cat - | tee >( nw_distance -sf -mp - > $tmpf )| nw_distance -sa -mp - >$tmpa

echo "
l = mean(read.csv('"$tmpf"',sep= ' ',header=F)\$V1)
b = mean(read.csv('"$tmpa"',sep= ' ',header=F)\$V1)
cat( if ( b > l) 1 else  (-2 * b^3+5 * b^2* l-3 *b* l^2+2 * sqrt(2) * sqrt(-b^2* (b-l)^3 * l))/(b * (b-l) * l) )
" | R --vanilla -q --slave

echo

rm $tmpf
rm $tmpa
