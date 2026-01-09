# تثبيت Java 11
# تثبيت Maven
# إعداد SSH
# تحميل Hadoop 3.3.1
# إعداد Hadoop
hadoop-env.sh
 إعداد core-site.xml
  إعداد hdfs-site.xml
# تهيئة وتشغيل HDFS
hdfs namenode -format
start-dfs.sh

# تثبيت Spark
cd ~
wget https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
tar -xzf spark-3.5.0-bin-hadoop3.tgz
mv spark-3.5.0-bin-hadoop3 spark
 # WordCount 
echo "hello spark hadoop" > file1.txt
hdfs dfs -put file1.txt /

# تشغيل Spark-shell 
rania@DESKTOP-DA06H1I:~$ spark-shell
26/01/08 23:50:57 WARN Utils: Your hostname, DESKTOP-DA06H1I resolves to a loopback address: 127.0.1.1; using 172.29.236.210 instead (on interface eth0)
26/01/08 23:50:57 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
26/01/08 23:51:07 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Spark context Web UI available at http://172.29.236.210:4040
Spark context available as 'sc' (master = local[*], app id = local-1767912668822).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.0
      /_/

Using Scala version 2.12.18 (OpenJDK 64-Bit Server VM, Java 11.0.29)
Type in expressions to have them evaluated.
Type :help for more information.

scala>


# Maven + Spark Java
فتح pom.xml تعديل dependencies
وproperties Java version

# إعداد YARN
yarn-site.xml
mapred-site.xml
# تشغيل yarn
start-yarn.sh

###  إنشاء ملف ورفعه إلى HDFS

nano file1.txt
hello spark hello hadoop spark hello
hdfs dfs -put file1.txt /
hdfs dfs -ls /
#  WordCount باستخدام Spark Batch (Java)
# إنشاء مشروع Maven 
mvn archetype:generate
cd wordcount-spark
# هيكلة المشروع
wordcount-spark/
├── pom.xml
├── src/main/java/spark/batch/WordCountTask.java
└── target/
# بناء المشروع
mvn clean package
# النتيجة
target/wordcount-spark-1.0-SNAPSHOT.jar
# تشغيل Spark Batch
spark-submit \
--class spark.batch.WordCountTask \
target/wordcount-spark-1.0-SNAPSHOT.jar \
hdfs://localhost:9000/file1.txt \
hdfs://localhost:9000/wc-output
# النتيجة
تنفيذ WordCount بنجاح

تخزين النتائج في HDFS
# عرض النتائج
hdfs dfs -cat /wc-output/part-00000
 
 (hello,3)
(spark,2)
(hadoop,1)
### المرحلة 4: Spark Structured Streaming (Socket)
# تشغيل Socket (Netcat)
nc -lk 9999
# تشغيل Streaming
spark-submit streaming.py
# إدخال بيانات مباشرة
hello world spark streaming hello
# النتيجة
+---------+-----+
|word     |count|
+---------+-----+
|hello    |2    |
|spark    |2    |
|streaming|1    |
+---------+-----+

