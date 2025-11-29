
PS C:\Users\rania> cd C:\kafka_2.13-3.9.0
>> .\bin\windows\kafka-topics.bat --create --topic iot-machines --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
>>
Created topic iot-machines.
PS C:\kafka_2.13-3.9.0> .\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
>>
iot-machines
PS C:\kafka_2.13-3.9.0>