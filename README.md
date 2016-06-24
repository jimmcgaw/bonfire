# Apache Spark with Python

Playing around with Spark using pyspark.

I've extracted the [Spark source](http://spark.apache.org/downloads.html) into my home directory (I've
got version 1.6.1) and set up my PATH as such in my .profile:

``` export PATH=$PATH:$HOME/spark-1.6.1/bin ```

``` export SPARK_HOME=$HOME/spark-1.6.1 ```

You'll also need Java. You should probably grab Scala and install it as well, even though I
don't plan to use it yet.

I assume, whoever you are, that you have Python 2.6+ installed. (I generally run 2.7.)

## Running

With the PATH set up above, you should be able to run:

``` $ spark-submit trump.py ```

This does a simple word count of a text dump of Trump's speeches. (source: [here](https://github.com/ryanmcdermott/trump-speeches))
