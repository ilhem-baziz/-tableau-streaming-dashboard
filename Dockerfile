FROM ubuntu:18.04

WORKDIR /home/mongobi

RUN apt-get update && \
    apt-get install -y libssl1.0.0 libssl-dev libgssapi-krb5-2 wget && \
    wget https://info-mongodb-com.s3.amazonaws.com/mongodb-bi/v2/mongodb-bi-linux-x86_64-ubuntu1804-v2.13.1.tgz && \
    tar -xvzf mongodb-bi-linux-x86_64-ubuntu1804-v2.13.1.tgz && \
    install -m755 mongodb-bi-linux-x86_64-ubuntu1804-v2.13.1/bin/mongo* /usr/local/bin/

CMD ["mongosqld","--mongo-uri=mongodb://ilhem:ilhem@mongodb:27017/streaming?authSource=admin", "--addr=0.0.0.0:3307","--logPath=/logs/mongosqld.log", "--logAppend"]
