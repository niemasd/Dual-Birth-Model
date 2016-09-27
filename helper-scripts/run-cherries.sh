#!/bin/bash

for s in 128 256 1024; do 
	for x in 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576; do 
		for i in {1..10}; do 
			echo -n "$s $x "; 
			python Alu-Project/tools/AluSimulator.py 1024 $x $s|nw_topology -|sed -e "s/[0-9]*//g"|grep -o "(,)"|wc -l; 
		done; 
	done; 
done | tee exp.stat


echo '

d=read.csv("exp.stat",sep=" ",head=F)

qplot(V2/1024,V3/V1,data=d,geom=c("boxplot"),group=c(V2/1024))+theme_bw()+scale_color_brewer(name="",palette="Set2") + scale_x_log10(limits=c(0.0005,2000))+ stat_function(fun = function(x) {r=10^(x);sqrt(r)/(r+sqrt(r)+1)}, colour = "red",size=1,linetype=2)+xlab(expression(r==lambda[a]/lambda[b]~(log~scale)))+ylab("cherry frequency")+facet_wrap(~V1)+geom_hline(yin=1/3,color="blue",linetype=3,size=1); ' |R --save
