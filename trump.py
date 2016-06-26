from pyspark import SparkContext, SparkConf
from operator import add

conf = SparkConf().setAppName('Trump Counter')
sc = SparkContext()

textFile = sc.textFile('./speeches.txt')
tokenizedFileData = textFile.flatMap(lambda line: line.split(' '))
countPrep = tokenizedFileData.map(lambda word: (word, 1))
counts = countPrep.reduceByKey(add).collect()
sortedCounts = sorted(counts, key=lambda wordCount: wordCount[1], reverse=True)

print sortedCounts

# shorthand for all of this we did above
# print tokenizedFileData.countByValue()

# print sc.parallelize(range(1, 101))
