#!/bin/bash

tmpa=`mktemp XXXX`
tmpf=`mktemp XXXX`

cat - | tee >( nw_distance -sf -mp - > $tmpf )| nw_distance -si -mp - |sed '$ d' >$tmpa

echo "
l = mean(read.csv('"$tmpf"',sep= ' ',header=F)\$V1)
i = mean(read.csv('"$tmpa"',sep= ' ',header=F)\$V1)
#cat( if ( b > l) 1 else  ( 1 - sqrt(2*(1-b/l)) )^2 )
cat( if ( i > l) 1 else  ( 1 - sqrt((1-i/l)) )^2 )
" | R --vanilla -q --slave

echo

rm $tmpf $tmpa 
