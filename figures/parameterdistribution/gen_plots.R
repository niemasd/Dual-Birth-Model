# load requirements
cat("Loading requirements...")
require(ggplot2)

# load input files
cat("\nLoading dist_all.stat...")
dist=read.csv("dist_all.stat",sep=' ',h=F)
cat(" done\nLoading unorddist_all.stat...")
unorddist=read.csv("unorddist_all.stat",sep=' ',h=F)
cat(" done\nLoading unrankdist_all.stat...")
unrankdist=read.csv("unrankdist_all.stat",sep=' ',h=F)
cat(" done\n\n")

# generate plots
cat("Generating dist.pdf... ")
ggplot(aes(x=reorder(interaction(V1,V2,V4),V5)),data=dist)+geom_bar(aes(y=V6/V3),stat="identity",fill="grey90",colour="black")+geom_line(aes(y=V5,group=interaction(V1,V2)),color="red",size=1,)+facet_wrap(~interaction(V1,V2,sep=","),scales="free",shrink=T,drop=T)+theme_bw()+theme(axis.text.x=element_blank(),panel.grid.minor=element_blank())+xlab("(a) 120 ranked ordered tree shapes with 6 leaves")+ylab("probability (frequency)");
ggsave("dist.pdf");
cat("Generating unorddist.pdf... ")
ggplot(aes(x=reorder(interaction(V1,V2,V4),V5)),data=unorddist)+geom_bar(aes(y=V6/V3),stat="identity",fill="grey90",colour="black")+geom_line(aes(y=V5,group=interaction(V1,V2)),color="red",size=1,)+facet_wrap(~interaction(V1,V2,sep=","),nrow=1,scales="free",shrink=T,drop=T)+theme_bw()+theme(axis.text.x=element_blank(),panel.grid.minor=element_blank())+xlab("(b) 16 ranked unordered tree shapes with 6 leaves")+ylab("probability (frequency)");
ggsave("unorddist.pdf");
cat("Generating unrankdist.pdf... ")
ggplot(aes(x=reorder(interaction(V1,V2,V4),V5)),data=unrankdist)+geom_bar(aes(y=V6/V3),stat="identity",fill="grey90",colour="black")+geom_line(aes(y=V5,group=interaction(V1,V2)),color="red",size=1,)+facet_wrap(~interaction(V1,V2,sep=","),nrow=1,scales="free",shrink=T,drop=T)+theme_bw()+theme(axis.text.x=element_blank(),panel.grid.minor=element_blank())+xlab("(c) 6 unranked unordered tree shapes with 6 leaves")+ylab("probability (frequency)");
ggsave("unrankdist.pdf");

# delete useless Rplots.pdf file
invisible(capture.output(file.remove("Rplots.pdf")));
