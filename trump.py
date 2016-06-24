from pyspark import SparkContext
from operator import add

sc = SparkContext()

textFile = sc.textFile('./speeches.txt')
tokenizedFileData = textFile.flatMap(lambda line: line.split(' '))
countPrep = tokenizedFileData.map(lambda word: (word, 1))
counts = countPrep.reduceByKey(add).collect()
sortedCounts = sorted(counts, key=lambda wordCount: wordCount[1], reverse=True)

print sortedCounts
