setwd("~/Documents/Na-transport-genes/")

genes.table <- read.table("Na-genes-table.tdt", header=TRUE, row.names="Genome")

distances <- dist(genes.table, method="binary")

clusters <- hclust(distances, method="ward")

plot(clusters, labels=FALSE)

filtered.genes.table <- read.table("Na-genes-table-filtered.tdt", header=TRUE, row.names="Genome")

filtered.distances <- dist(filtered.genes.table, method="binary")

filtered.clusters <- hclust(filtered.distances, method="ward")

plot(filtered.clusters, labels=FALSE)
