#!/bin/bash

set -x

f=$1
t=$2

c=$(sed -e "s/):/)1.0:/g" $f|nw_ed - 'i & b<'$t' ' o | nw_topology -IL -|grep -o "(,*)"|wc -l)

echo "scale=5;"$c / `nw_stats $f|grep leaves|cut -f2`|bc
