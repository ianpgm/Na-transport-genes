setwd("~/Documents/Na-transport-genes/")

genes.table <- read.table("Na-genes-table.tdt", header=TRUE, row.names="Genome")

distances <- dist(genes.table, method="binary")

clusters <- hclust(distances, method="ward")

plot(clusters, labels=FALSE)

filtered.genes.table <- read.table("Na-genes-table-filtered.tdt", header=TRUE, row.names="Genome")

filtered.distances <- dist(filtered.genes.table, method="binary")

filtered.clusters <- hclust(filtered.distances, method="ward")

plot(filtered.clusters, labels=FALSE)

filtered.genes.table <- read.table("Na-genes-table-ATPion-filtered.tdt", header=TRUE, row.names="Genome")

filtered.distances <- dist(filtered.genes.table, method="binary")

filtered.clusters <- hclust(filtered.distances, method="ward")

plot(filtered.clusters, labels=FALSE)

gene.centric.table <- t(filtered.genes.table)
gc.distances <- dist(gene.centric.table, method="binary")
gc.clusters <- hclust(gc.distances, method="ward")
plot(gc.clusters)

ATPion = filtered.genes.table$ATPion
MtrA = filtered.genes.table$MtrA

AyMy = 0
AyMn = 0
AnMn = 0
AnMy = 0

for(i in 1:length(MtrA))
{
	if(ATPion[i] == 1)
	{
		if(MtrA[i] == 1)
		{
			AyMy = AyMy + 1
		}
		if(MtrA[i] == 0)
		{
			AyMn = AyMn + 1
		}
	}
	if(ATPion[i] == 0)
	{
		if(MtrA[i] == 1)
		{
			AnMy = AnMy + 1
		}
		if(MtrA[i] == 0)
		{
			AnMn = AnMn + 1
		}
	}
}