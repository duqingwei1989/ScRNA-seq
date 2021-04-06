protoplast_rpkm <-  read.table('/proto_fpkm_matrix.csv',header=T,row.names=1,sep=',')
protoplast_rpkm_statistics <- transform(protoplast_rpkm, mean=apply(protoplast_rpkm,1,mean), sd=apply(protoplast_rpkm,1,sd), sum=apply(protoplast_rpkm,1,sum), gene =row.names(protoplast_rpkm))
protoplast_rpkm_statistics$CV <-protoplast_rpkm_statistics$sd/protoplast_rpkm_statistics$mean