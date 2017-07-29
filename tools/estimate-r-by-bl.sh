#!/bin/bash

tmp=`mktemp $TMPDIR/R"XXXX"`
nw_distance -n -sa -mp -|sed -e "s/^I/I /" -e "s/^L/L /"|awk '{print $3,$1}' > $tmp

echo "
tmp=read.csv('"$tmp"',sep= ' ',header=F)
attach(tmp)
l = mean(tmp[V2=='L', 1])
b = mean(V1)
if ( b > l) {
	cat( 1 )
} else {
	cat(   (-2 * b^3+5 * b^2* l-3 *b* l^2+2 * sqrt(2) * sqrt(-b^2* (b-l)^3 * l))/(b * (b-l) * l) )
}
" | R --vanilla -q --slave

echo
